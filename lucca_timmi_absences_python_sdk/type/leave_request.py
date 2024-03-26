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

from lucca_timmi_absences_python_sdk.type.cancellation_request import CancellationRequest
from lucca_timmi_absences_python_sdk.type.leave_period import LeavePeriod
from lucca_timmi_absences_python_sdk.type.leave_request_approval import LeaveRequestApproval

class RequiredLeaveRequest(TypedDict):
    pass

class OptionalLeaveRequest(TypedDict, total=False):
    # Unique identifier for the LeaveRequest
    id: int

    # Unique identifier for the attached LeavePeriod
    leavePeriodId: int

    leavePeriod: LeavePeriod

    # Status of the Leave request. Can be :   0 = PENDING_APPROVAL  2 = APPROVED  3 = DENIED  4 = CANCELLED  5 = CANCELLATION_PENDING 
    status: typing.Union[int, float]

    # Time at which the object was created
    creationDate: datetime

    # Unique identifier for the next approver
    nextApproverId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Unique identifier for the user that cancelled the Leave Request
    cancellationUserId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Time at which the object was cancelled
    cancellationDate: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Has the value `true` for acitve Leave Request or the value `false` for cancelled Leave Request
    isActive: bool

    approvals: typing.List[LeaveRequestApproval]

    cancellationRequests: typing.List[CancellationRequest]

class LeaveRequest(RequiredLeaveRequest, OptionalLeaveRequest):
    pass
