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
from lucca_timmi_absences_python_sdk.type.leave_period_log import LeavePeriodLog

class RequiredLeavePeriod(TypedDict):
    pass

class OptionalLeavePeriod(TypedDict, total=False):
    # Unique identifier for the LeavePeriod
    id: typing.Union[int, float]

    # Unique identifier for the user 
    ownerId: typing.Union[int, float]

    # Has the value `true` for approved LeavePeriod or the value `false` for LeavePeriod pending approval
    isConfirmed: bool

    # Time at which the LeavePeriod was approved
    confirmationDate: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Unique identifier for the attached document
    attachmentId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    leaves: 'typing.List[Leave]'

    logs: typing.List[LeavePeriodLog]

class LeavePeriod(RequiredLeavePeriod, OptionalLeavePeriod):
    pass
