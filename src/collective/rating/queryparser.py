# -*- coding: utf-8 -*-


def _floatEqual(context, row):
    values = None
    if type(row.values) is list:
        values = [float(v) for v in row.values]
    elif type(row.values) is str:
        values = float(row.values)
    return {row.index: {"query": values}}


def _floatLessThan(context, row):
    value = None
    if type(row.values) is str:
        value = float(row.values)
    tmp = {row.index: {"query": value, "range": "max"}}
    return tmp


def _floatLargerThan(context, row):
    value = None
    if type(row.values) is str:
        value = float(row.values)
    tmp = {row.index: {"query": value, "range": "min"}}
    return tmp
