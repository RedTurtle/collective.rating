# # -*- coding: utf-8 -*-
# from collective.rating.behaviors.rating import IRating
# from collective.rating.browser.manage_rating import KEY as KEY_value
# from collective.rating.browser.manage_rating import KEY_avg
# from functools import reduce
# from persistent.dict import PersistentDict
# from plone.indexer.decorator import indexer
# from zope.annotation.interfaces import IAnnotations
#
#
# def _storage_value(item):
#     if item:
#         annotations = IAnnotations(item)
#         if KEY_value not in annotations:
#             annotations[KEY_value] = PersistentDict({})
#         return annotations[KEY_value]
#
#
# def _storage_avg(item):
#     if item:
#         annotations = IAnnotations(item)
#         if KEY_avg not in annotations:
#             annotations[KEY_avg] = PersistentDict({})
#         return annotations[KEY_avg]
#
#
# def rating_list(annotations):
#     return map(lambda x: x['rating_value'], annotations.values())
#
#
# @indexer(IRating)
# def avg_rating(object, **kw):
#     annotations_value = _storage_value(object)
#     annotations_avg = _storage_avg(object)
#     if annotations_value:
#         num_rating = len(annotations_value.keys())
#         sum_rating = reduce(
#             (lambda x, y: float(x) + float(y)),
#             rating_list(annotations_value))
#         result = (float(float(sum_rating) / num_rating), num_rating)
#
#         annotations_avg[object.UID()] = {
#             'avg': result,
#         }
#         return result
#     else:
#         result = (0, 0)
#
#         annotations_avg[object.UID()] = {
#             'avg': result,
#         }
#         return result
