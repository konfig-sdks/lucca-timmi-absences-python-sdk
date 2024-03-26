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


class RequiredLeaveRequestApproval(TypedDict):
    pass

class OptionalLeaveRequestApproval(TypedDict, total=False):
    # Unique identifier for the LeaveRequestApproval
    id: int

    date: datetime

    # Unique identifier for the approver
    approverId: typing.Union[int, float]

    # 0 = PENDING_APPROVAL  2 = APPROVED  3 = DENIED  4 = CANCELLED  5 = CANCELLATION_PENDING 
    substitutedApproverId: int

    # Has the value `true` for approved LeaveRequest or the value `false` for LeaveRequest pending approval
    approved: bool

    # Comments
    comment: str

class LeaveRequestApproval(RequiredLeaveRequestApproval, OptionalLeaveRequestApproval):
    pass
