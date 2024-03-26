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


class CancellationRequest(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    author_id: typing.Optional[int] = Field(None, alias='authorId')

    comment: typing.Optional[str] = Field(None, alias='comment')

    # 0 = PENDING_APPROVAL  2 = APPROVED  3 = DENIED  4 = CANCELLED  5 = CANCELLATION_PENDING 
    rank: typing.Optional[Literal[0, 2, 3, 4, 5]] = Field(None, alias='rank')

    approved: typing.Optional[bool] = Field(None, alias='approved')

    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    next_approver_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='nextApproverId')

    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
