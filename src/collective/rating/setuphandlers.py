# -*- coding: utf-8 -*-
from collective.rating import logger
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return ["collective.rating:uninstall"]


def post_install(context):
    """Post install script"""

    portal = api.portal.get()
    setup_tool = portal.portal_setup
    setup_tool.runImportStepFromProfile(
        "profile-collective.rating:default", "catalog"
    )
    catalog = api.portal.get_tool(name=u"portal_catalog")
    indexes = catalog.indexes()

    wanted = [("avg-rating", "FieldIndex", {"indexed_attrs": "avg-rating"})]

    indexables = []
    for idx in wanted:
        if idx[0] in indexes:
            logger.info(
                "Found the {0} index in the catalog, nothing "
                "changed.".format(idx[0])
            )
        else:
            catalog.addIndex(name=idx[0], type=idx[1], extra=idx[2])
            logger.info(
                "Added {0} ({1}) to the catalog.".format(idx[0], idx[1])
            )
            indexables.append(idx[0])
    if len(indexables) > 0:
        logger.info("Indexing new indexes {0}.".format(", ".join(indexables)))
        catalog.manage_reindexIndex(ids=indexables)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
