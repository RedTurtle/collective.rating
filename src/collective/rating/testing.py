# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.rating


class CollectiveRatingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.rating)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.rating:default')


COLLECTIVE_RATING_FIXTURE = CollectiveRatingLayer()


COLLECTIVE_RATING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_RATING_FIXTURE,),
    name='CollectiveRatingLayer:IntegrationTesting'
)


COLLECTIVE_RATING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_RATING_FIXTURE,),
    name='CollectiveRatingLayer:FunctionalTesting'
)


COLLECTIVE_RATING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_RATING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveRatingLayer:AcceptanceTesting'
)
