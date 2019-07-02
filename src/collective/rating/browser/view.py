# -*- coding: utf-8 -*-
from collective.rating.behaviors.rating import IRating
from plone.app.contenttypes.browser.collection import CollectionView

import json


class RatingCollectionView(CollectionView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getRating(self, item):
        item_obj = item._brain.getObject()
        if item_obj:
            return json.dumps(
                {
                    "number_of_ratings": IRating(item_obj).num_rating(),
                    "rating": IRating(item_obj).avg_rating(),
                    "max_rating": item_obj.max_rating,
                }
            )
        return 0
