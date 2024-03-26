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


class ImportsReplaceEntitlementsRequest(BaseModel):
    file: typing.Optional[str] = Field(None, alias='File')

    # Description of the entries generated by the import (visible to users in the account details).
    description: typing.Optional[str] = Field(None, alias='Description')

    # Reference date (text mode). Respect the format: yyyy-MM-ddThh: mm: ss
    reference_date: typing.Optional[datetime] = Field(None, alias='ReferenceDate')

    # Types of entries to take into account, separated by commas, from the following list: AutoAccruals, ManualAccruals, Regularisations, EntitlementsImport, Seniority, Fractionnement, TimeSavings, Comp  By default: `AutoAccruals, ManualAccruals, Regularizations` which correspond to the main cases of acquisition (automatic acquisition, manual adjustments, regularisations).
    entry_types: typing.Optional[str] = Field(None, alias='EntryTypes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
