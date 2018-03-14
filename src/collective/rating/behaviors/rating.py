# -*- coding: utf-8 -*-
from collective.rating import _
from collective.rating.browser.settings import ISettingsSchema
from persistent.dict import PersistentDict
from plone import api
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.annotation.interfaces import IAnnotations
from zope.interface import alsoProvides
from zope.interface import Interface


KEY = 'collective.rating.values'


def default_stars():
    return api.portal.get_registry_record('default_stars', ISettingsSchema)


class IRatingLayer(Interface):
    """ behaviors interface """


class IRating(model.Schema):
    """ Interface for rate """

    model.fieldset(
        u'Rating field',
        label=_(u'Rating\'s field'),
        fields=[
            u'active_rating',
            u'max_rating',
        ]
    )

    active_rating = schema.Bool(
        title=_(u'active_rating_title', default=u'Rating is active'),
        default=True,
        required=True,
    )

    max_rating = schema.Int(
        title=_(u'max_rating_title', default=u'Num of stars'),
        required=True,
        defaultFactory=default_stars,
    )

    def avg_rating():
        """ return avg of rating """

    def num_rating():
        """ return num of rating """


alsoProvides(IRating, IFormFieldProvider)


class Rating(object):

    def __init__(self, context):
        self.context = context

    @property
    def active_rating(self):
        return self.context.active_rating

    @active_rating.setter
    def active_rating(self, value):
        self.context.active_rating = value

    @property
    def max_rating(self):
        return self.context.max_rating

    @max_rating.setter
    def max_rating(self, value):
        self.context.max_rating = value

    def _storage(self, item):
        if item:
            annotations = IAnnotations(item)
            if KEY not in annotations:
                annotations[KEY] = PersistentDict({})
            return annotations[KEY]

    def num_rating(self):
        annotations = self._storage(self.context)
        return len(annotations.keys())

    def rating_list(self, annotations):
        return map(lambda x: x['rating_value'], annotations.values())

    def avg_rating(self):
        annotations = self._storage(self.context)
        if annotations:
            num_rating = len(annotations.keys())
            sum_rating = reduce(
                (lambda x, y: float(x) + float(y)),
                self.rating_list(annotations))
            return float(float(sum_rating) / num_rating)
        else:
            return 0
