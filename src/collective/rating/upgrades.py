# -*- coding: utf-8 -*-
from collective.rating import logger
from plone import api

import transaction

default_profile = "profile-collective.rating:default"


def migrate_to_1001(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runImportStepFromProfile(default_profile, "plone.app.registry")
    logger.info(u"Updated to 1001")


def migrate_to_1002(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runImportStepFromProfile(default_profile, "plone.app.registry")
    setup_tool.runImportStepFromProfile(default_profile, "catalog")

    pc = api.portal.get().portal_catalog

    objs = api.content.find(
        object_provides="collective.rating.behaviors.rating.IRatingLayer"
    )
    for obj in objs:
        pc.catalog_object(obj, idxs=["avg-rating"])

    transaction.commit()

    logger.info(u"Updated to 1002")


def migrate_to_1003(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runImportStepFromProfile(default_profile, "typeinfo")
    logger.info(u"Updated to 1003")
