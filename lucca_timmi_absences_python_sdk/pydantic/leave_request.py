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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lucca_timmi_absences_python_sdk.pydantic.cancellation_request import CancellationRequest
from lucca_timmi_absences_python_sdk.pydantic.leave_period import LeavePeriod
from lucca_timmi_absences_python_sdk.pydantic.leave_request_approval import LeaveRequestApproval

class LeaveRequest(BaseModel):
    # Unique identifier for the LeaveRequest
    id: typing.Optional[int] = Field(None, alias='id')

    # Unique identifier for the attached LeavePeriod
    leave_period_id: typing.Optional[int] = Field(None, alias='leavePeriodId')

    leave_period: typing.Optional[LeavePeriod] = Field(None, alias='leavePeriod')

    # Status of the Leave request. Can be :   0 = PENDING_APPROVAL  2 = APPROVED  3 = DENIED  4 = CANCELLED  5 = CANCELLATION_PENDING 
    status: typing.Optional[Literal[0, 2, 3, 4, 5]] = Field(None, alias='status')

    # Time at which the object was created
    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    # Unique identifier for the next approver
    next_approver_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='nextApproverId')

    # Unique identifier for the user that cancelled the Leave Request
    cancellation_user_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='cancellationUserId')

    # Time at which the object was cancelled
    cancellation_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='cancellationDate')

    # Has the value `true` for acitve Leave Request or the value `false` for cancelled Leave Request
    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    approvals: typing.Optional[typing.List[LeaveRequestApproval]] = Field(None, alias='approvals')

    cancellation_requests: typing.Optional[typing.List[CancellationRequest]] = Field(None, alias='cancellationRequests')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
