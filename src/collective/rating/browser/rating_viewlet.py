# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase


class RatingManagerViewlet(ViewletBase):
    def rating_is_active(self):
        return self.context.active_rating

    def render(self):
        return self.index()

    def can_vote(self):
        if api.env.read_only_mode():
            return False
        return api.user.has_permission(
            "collective.rating: Vote a content",
            user=api.user.get_current(),
            obj=self.context,
        )
