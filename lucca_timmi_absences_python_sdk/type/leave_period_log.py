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


class RequiredLeavePeriodLog(TypedDict):
    pass

class OptionalLeavePeriodLog(TypedDict, total=False):
    id: int

    date: datetime

    comment: str

    # - 0 = PENDING_APPROVAL - 2 = APPROVED - 3 = DENIED - 4 = CANCELLED - 5 = CANCELLATION_PENDING 
    status: typing.Union[int, float]

class LeavePeriodLog(RequiredLeavePeriodLog, OptionalLeavePeriodLog):
    pass
