# -*- coding: utf-8 -*-
from collective.rating import logger
from plone import api


default_profile = 'profile-collective.rating:default'


def migrate_to_1001(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'plone.app.registry')
    logger.info(u'Updated to 1001')
