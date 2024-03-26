# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lucca_timmi_absences_python_sdk.type.leave import Leave

class RequiredLeavesGetApprovedListResponse(TypedDict):
    pass

class OptionalLeavesGetApprovedListResponse(TypedDict, total=False):
    data: Leave

class LeavesGetApprovedListResponse(RequiredLeavesGetApprovedListResponse, OptionalLeavesGetApprovedListResponse):
    pass
