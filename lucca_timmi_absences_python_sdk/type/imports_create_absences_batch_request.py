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

from lucca_timmi_absences_python_sdk.type.imports_create_absences_batch_request_files import ImportsCreateAbsencesBatchRequestFiles

class RequiredImportsCreateAbsencesBatchRequest(TypedDict):
    pass

class OptionalImportsCreateAbsencesBatchRequest(TypedDict, total=False):
    files: ImportsCreateAbsencesBatchRequestFiles

class ImportsCreateAbsencesBatchRequest(RequiredImportsCreateAbsencesBatchRequest, OptionalImportsCreateAbsencesBatchRequest):
    pass
