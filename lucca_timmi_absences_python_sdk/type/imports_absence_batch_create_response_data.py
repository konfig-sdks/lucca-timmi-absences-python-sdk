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

from lucca_timmi_absences_python_sdk.type.imports_absence_batch_create_response_data_report import ImportsAbsenceBatchCreateResponseDataReport

class RequiredImportsAbsenceBatchCreateResponseData(TypedDict):
    pass

class OptionalImportsAbsenceBatchCreateResponseData(TypedDict, total=False):
    id: str

    report: ImportsAbsenceBatchCreateResponseDataReport

    generatedAt: datetime

    # 0 = Pending  10 = Started  20 = Finished  100 = Failed 
    status: int

    lineTotal: int

    testErrorTotal: int

    totalStep: int

    expectedCreationTotal: int

    expectedUpdateTotal: int

    testNonBlockingErrorTotal: int

    currentStep: int

    creationTotal: int

    updateTotal: int

    importErrorTotal: int

class ImportsAbsenceBatchCreateResponseData(RequiredImportsAbsenceBatchCreateResponseData, OptionalImportsAbsenceBatchCreateResponseData):
    pass
