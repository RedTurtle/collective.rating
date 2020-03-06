# -*- coding: utf-8 -*-
from collective.rating.behaviors.rating import IRating
from collective.rating.utils import storage
from plone import api
from Products.Five import BrowserView

import json


class ManageRating(BrowserView):
    def update_rating(self):
        current_rating = self.request.get("current_rating", None)
        if current_rating:
            annotations = storage(self.context)
            username = api.user.get_current().getUserName()
            annotations[username] = {
                "user": username,
                "rating_value": current_rating,
            }

        # call catalog to update avg rating of obj
        pc = api.portal.get().portal_catalog
        pc.catalog_object(self.context, idxs=["avg-rating"])

    def delete_rating(self):
        annotations = storage(self.context)
        username = api.user.get_current().getUserName()
        if username in list(annotations.keys()):
            del annotations[username]
            return json.dumps({"ok": True})
        else:
            return json.dumps({"ok": False})

    def get_rating(self):
        annotations = storage(self.context)
        username = api.user.get_current().getUserName()
        if username in list(annotations.keys()):
            return json.dumps(
                {"current_value": annotations[username]["rating_value"]}
            )
        else:
            return json.dumps({"current_value": 0})

    def get_star_size(self):
        return json.dumps({"max_rating": self.context.max_rating})

    def get_avg_rating(self):
        avg_rating = IRating(self.context).avg_rating()
        num_rating = IRating(self.context).num_rating()
        return json.dumps({"avg_rating": avg_rating, "num_rating": num_rating})
