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


class LeavePeriodLog(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    date: typing.Optional[datetime] = Field(None, alias='date')

    comment: typing.Optional[str] = Field(None, alias='comment')

    # - 0 = PENDING_APPROVAL - 2 = APPROVED - 3 = DENIED - 4 = CANCELLED - 5 = CANCELLATION_PENDING 
    status: typing.Optional[Literal[0, 2, 3, 4, 5]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
