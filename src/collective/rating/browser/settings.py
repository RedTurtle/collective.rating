# -*- coding: utf-8 -*-
from collective.rating import _
from collective.rating.utils import storage
from plone import api
from plone import schema
from plone.app.registry.browser import controlpanel
from z3c.form import button
from zope.interface import Interface


class ISettingsSchema(Interface):
    default_stars = schema.Int(
        title=_(u'default_stars_title', default=u'Default stars number'),
        required=False,
        default=5,
    )


class RatingSettings(controlpanel.RegistryEditForm):
    schema = ISettingsSchema
    id = u'RatingSettings'
    label = _(u'rating_schema', default=u'Rating Settings')

    def updateFields(self):
        super(RatingSettings, self).updateFields()

    def updateWidgets(self):
        super(RatingSettings, self).updateWidgets()

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        super(RatingSettings, self).handleCancel(self, action)

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        self.save()

    def _new_vote(self, old_rating, new_max_rating, obj):
        return float(
            float(
                new_max_rating * float(old_rating)) / obj.max_rating)

    def update_rating(self, obj, value):
        if obj.max_rating != value:
            annotations = storage(obj)
            for user in annotations.keys():
                annotations[user] = {
                    'rating_value':  self._new_vote(
                        annotations[user]['rating_value'], value, obj),
                    'user': user,
                }
            obj.max_rating = value

    def save(self):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return False

        # controlli quali oggetti hanno la behaviors rating e aggiorno i dati
        catalog = api.portal.get_tool(name='portal_catalog')
        brains = catalog(
            object_provides='collective.rating.behaviors.rating.IRatingLayer')
        for brain in brains:
            self.update_rating(brain.getObject(), data['default_stars'])

        self.applyChanges(data)
        return True


class RatingSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = RatingSettings
