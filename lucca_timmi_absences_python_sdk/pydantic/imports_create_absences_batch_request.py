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

from lucca_timmi_absences_python_sdk.pydantic.imports_create_absences_batch_request_files import ImportsCreateAbsencesBatchRequestFiles

class ImportsCreateAbsencesBatchRequest(BaseModel):
    files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = Field(None, alias='files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
