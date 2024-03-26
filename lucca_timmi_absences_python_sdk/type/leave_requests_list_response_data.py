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

from lucca_timmi_absences_python_sdk.type.leave_request import LeaveRequest

class RequiredLeaveRequestsListResponseData(TypedDict):
    pass

class OptionalLeaveRequestsListResponseData(TypedDict, total=False):
    items: typing.List[LeaveRequest]

    count: int

class LeaveRequestsListResponseData(RequiredLeaveRequestsListResponseData, OptionalLeaveRequestsListResponseData):
    pass
