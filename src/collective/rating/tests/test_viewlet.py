# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.rating.testing import (  # noqa
    COLLECTIVE_RATING_INTEGRATION_TESTING,  # noqa
)  # noqa
from collective.rating.behaviors.rating import IRating
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.schema import SchemaInvalidatedEvent
from zope.component import queryUtility
from zope.event import notify

import unittest


class TestViewlet(unittest.TestCase):
    """Test that viewlet renders correctly."""

    layer = COLLECTIVE_RATING_INTEGRATION_TESTING

    def _enable_rating_behavior(self):
        fti = queryUtility(IDexterityFTI, name='Document')
        behaviors = list(fti.behaviors)
        behaviors.append(IRating.__identifier__)
        fti.behaviors = tuple(behaviors)
        # invalidate schema cache
        notify(SchemaInvalidatedEvent('Document'))

    def _disable_refresh_behavior(self):
        fti = queryUtility(IDexterityFTI, name='Document')
        behaviors = list(fti.behaviors)
        behaviors.remove(IRating.__identifier__)
        fti.behaviors = tuple(behaviors)
        # invalidate schema cache
        notify(SchemaInvalidatedEvent('Document'))

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.document = api.content.create(
            type='Document', title='Test document', container=self.portal
        )

    def test_viewlet_is_shown_if_behavior_is_enabled(self):
        """Test if collective.rating is enabled"""
        view = api.content.get_view(u'view', self.document, self.request)
        self.assertNotIn('manage-rating', view())
        self._enable_rating_behavior()
        self.assertIn('manage-rating', view())
