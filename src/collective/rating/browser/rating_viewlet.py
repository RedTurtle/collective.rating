# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase


class RatingManagerViewlet(ViewletBase):
    def rating_is_active(self):
        return self.context.active_rating

    def render(self):
        return self.index()

    def can_vote(self):
        permissions = api.user.get_permissions(user=api.user.get_current())
        return (
            permissions["collective.rating: Vote a content"]
            if permissions.get("collective.rating: Vote a content")
            else False
        )
