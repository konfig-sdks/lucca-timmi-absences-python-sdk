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

from lucca_timmi_absences_python_sdk.pydantic.imports_absence_batch_create_response_data_report import ImportsAbsenceBatchCreateResponseDataReport

class ImportsAbsenceBatchCreateResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    report: typing.Optional[ImportsAbsenceBatchCreateResponseDataReport] = Field(None, alias='report')

    generated_at: typing.Optional[datetime] = Field(None, alias='generatedAt')

    # 0 = Pending  10 = Started  20 = Finished  100 = Failed 
    status: typing.Optional[Literal[0, 10, 20, 100]] = Field(None, alias='status')

    line_total: typing.Optional[int] = Field(None, alias='lineTotal')

    test_error_total: typing.Optional[int] = Field(None, alias='testErrorTotal')

    total_step: typing.Optional[int] = Field(None, alias='totalStep')

    expected_creation_total: typing.Optional[int] = Field(None, alias='expectedCreationTotal')

    expected_update_total: typing.Optional[int] = Field(None, alias='expectedUpdateTotal')

    test_non_blocking_error_total: typing.Optional[int] = Field(None, alias='testNonBlockingErrorTotal')

    current_step: typing.Optional[int] = Field(None, alias='currentStep')

    creation_total: typing.Optional[int] = Field(None, alias='creationTotal')

    update_total: typing.Optional[int] = Field(None, alias='updateTotal')

    import_error_total: typing.Optional[int] = Field(None, alias='importErrorTotal')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
