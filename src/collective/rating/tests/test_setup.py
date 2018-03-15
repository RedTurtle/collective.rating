# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from collective.rating.testing import COLLECTIVE_RATING_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.rating is properly installed."""

    layer = COLLECTIVE_RATING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.rating is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.rating'))

    def test_browserlayer(self):
        """Test that ICollectiveRatingLayer is registered."""
        from collective.rating.interfaces import (
            ICollectiveRatingLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveRatingLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RATING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_NAME)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.rating'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.rating is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.rating'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRatingLayer is removed."""
        from collective.rating.interfaces import \
            ICollectiveRatingLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveRatingLayer,
            utils.registered_layers())
