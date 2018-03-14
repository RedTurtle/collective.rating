# -*- coding: utf-8 -*-
from collective.rating import _
from plone import schema
from plone.app.registry.browser import controlpanel
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


class RatingSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = RatingSettings
