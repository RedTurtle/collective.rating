# -*- coding: utf-8 -*-
from persistent.dict import PersistentDict
from zope.annotation.interfaces import IAnnotations


KEY = 'collective.rating.values'


def storage(item):
    if item:
        annotations = IAnnotations(item)
        if KEY not in annotations:
            annotations[KEY] = PersistentDict({})
        return annotations[KEY]
