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

from lucca_timmi_absences_python_sdk.pydantic.leave_account import LeaveAccount
if TYPE_CHECKING:
    from lucca_timmi_absences_python_sdk.pydantic.leave_period import LeavePeriod

class Leave(BaseModel):
    # Unique identifier for the Leave
    id: str = Field(alias='id')

    # Date of the leave in ISO format `yyyy-mm-dd`
    date: date = Field(alias='date')

    # Has the value `true` for morning or the value `false` for afternoon
    is_am: bool = Field(alias='isAm')

    # Unique identifier for the attached LeaveAccount
    leave_account_id: int = Field(alias='leaveAccountId')

    # Unique identifier for the attached LeavePeriod
    leave_period_id: int = Field(alias='leavePeriodId')

    leave_account: typing.Optional[LeaveAccount] = Field(None, alias='leaveAccount')

    leave_period: typing.Optional['LeavePeriod'] = Field(None, alias='leavePeriod')

    # Leave duration in hours
    value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='value')

    # Time at which the object was created
    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    # Has the value `true` when the Leave exists (for pending or confirmed LeavePeriods), or the value `false` when it has been deleted (for canceled or denied LeaveRequests). 
    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    # Time at which the request was canceled
    cancellation_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='cancellationDate')

    # Unique identifier for the user who canceled the request 
    cancellation_user_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='cancellationUserId')

    # Comments
    comment: typing.Optional[str] = Field(None, alias='comment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
