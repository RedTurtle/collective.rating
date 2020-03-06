# -*- coding: utf-8 -*-
from collective.rating.behaviors.rating import IRatingLayer, IRating
from plone.indexer.decorator import indexer


@indexer(IRatingLayer)
def avg_rating(object, **kw):
    return IRating(object).avg_rating()
