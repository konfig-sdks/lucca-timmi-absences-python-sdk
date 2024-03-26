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

from lucca_timmi_absences_python_sdk.pydantic.leave import Leave
from lucca_timmi_absences_python_sdk.pydantic.leave_period_log import LeavePeriodLog

class LeavePeriod(BaseModel):
    # Unique identifier for the LeavePeriod
    id: typing.Optional[typing.Union[int, float]] = Field(None, alias='id')

    # Unique identifier for the user 
    owner_id: typing.Optional[typing.Union[int, float]] = Field(None, alias='ownerId')

    # Has the value `true` for approved LeavePeriod or the value `false` for LeavePeriod pending approval
    is_confirmed: typing.Optional[bool] = Field(None, alias='isConfirmed')

    # Time at which the LeavePeriod was approved
    confirmation_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='confirmationDate')

    # Unique identifier for the attached document
    attachment_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='attachmentId')

    leaves: typing.Optional['typing.List[Leave]'] = Field(None, alias='leaves')

    logs: typing.Optional[typing.List[LeavePeriodLog]] = Field(None, alias='logs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
