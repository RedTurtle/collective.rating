# -*- coding: utf-8 -*-
from collective.rating.behaviors.rating import IRating
from collective.rating.behaviors.rating import KEY
from persistent.dict import PersistentDict
from plone import api
from Products.Five import BrowserView
from zope.annotation.interfaces import IAnnotations

import json


class ManageRating(BrowserView):

    def _storage(self, item):
        if item:
            annotations = IAnnotations(item)
            if KEY not in annotations:
                annotations[KEY] = PersistentDict({})
            return annotations[KEY]

    def update_rating(self):
        current_rating = self.request.get('current_rating', None)
        if current_rating:
            annotations = self._storage(self.context)
            username = api.user.get_current().getUserName()
            annotations[username] = {
                'user': username,
                'rating_value': current_rating,
            }

    def delete_rating(self):
        annotations = self._storage(self.context)
        username = api.user.get_current().getUserName()
        if username in annotations.keys():
            del annotations[username]
            return json.dumps({'ok': True})
        else:
            return json.dumps({'ok': False})

    def get_rating(self):
        annotations = self._storage(self.context)
        username = api.user.get_current().getUserName()
        if username in annotations.keys():
            return json.dumps(
                {'current_value': annotations[username]['rating_value']}
            )
        else:
            return json.dumps({'current_value': 0})

    def get_star_size(self):
        return json.dumps({
            'max_rating': self.context.max_rating,
        })

    def get_avg_rating(self):
        avg_rating = IRating(self.context).avg_rating()
        num_rating = IRating(self.context).num_rating()
        return json.dumps({
            'avg_rating': avg_rating,
            'num_rating': num_rating,
        })
