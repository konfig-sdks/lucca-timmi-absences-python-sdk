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

from lucca_timmi_absences_python_sdk.type.leave_account import LeaveAccount
if TYPE_CHECKING:
    from lucca_timmi_absences_python_sdk.type.leave_period import LeavePeriod

class RequiredLeave(TypedDict):
    # Unique identifier for the Leave
    id: str

    # Date of the leave in ISO format `yyyy-mm-dd`
    date: date

    # Has the value `true` for morning or the value `false` for afternoon
    isAm: bool

    # Unique identifier for the attached LeaveAccount
    leaveAccountId: int

    # Unique identifier for the attached LeavePeriod
    leavePeriodId: int

class OptionalLeave(TypedDict, total=False):
    leaveAccount: LeaveAccount

    leavePeriod: 'LeavePeriod'

    # Leave duration in hours
    value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Time at which the object was created
    creationDate: datetime

    # Has the value `true` when the Leave exists (for pending or confirmed LeavePeriods), or the value `false` when it has been deleted (for canceled or denied LeaveRequests). 
    isActive: bool

    # Time at which the request was canceled
    cancellationDate: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Unique identifier for the user who canceled the request 
    cancellationUserId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Comments
    comment: str

class Leave(RequiredLeave, OptionalLeave):
    pass
