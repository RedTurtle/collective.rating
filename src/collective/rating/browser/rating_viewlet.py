# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase


class RatingManagerViewlet(ViewletBase):

    def rating_is_active(self):
        return self.context.active_rating

    def render(self):
        return self.index()
