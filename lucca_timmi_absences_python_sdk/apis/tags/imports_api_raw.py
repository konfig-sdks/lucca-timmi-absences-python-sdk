# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_timmi_absences_python_sdk.paths.api_v3_services_import_leave_periods.post import AbsenceBatchCreateRaw
from lucca_timmi_absences_python_sdk.paths.timmi_absences_api_imports_v1_0_leave_periods.post import CreateAbsencesBatchRaw
from lucca_timmi_absences_python_sdk.paths.figgo_api_public_services_v1_0_leave_entitlements_import.post import EntitlementsBatchImportRaw
from lucca_timmi_absences_python_sdk.paths.timmi_absences_api_imports_v1_0_leave_periods_summary_id_progress.get import GetProgressRaw
from lucca_timmi_absences_python_sdk.paths.timmi_absences_api_public_services_v1_0_leave_entitlements_import.post import ImportLeaveEntitlementsRaw
from lucca_timmi_absences_python_sdk.paths.figgo_api_public_services_v1_0_leave_entitlements_replace.post import ReplaceEntitlementsRaw
from lucca_timmi_absences_python_sdk.paths.timmi_absences_api_public_services_v1_0_leave_entitlements_replace.post import ReplaceEntitlements0Raw


class ImportsApiRaw(
    AbsenceBatchCreateRaw,
    CreateAbsencesBatchRaw,
    EntitlementsBatchImportRaw,
    GetProgressRaw,
    ImportLeaveEntitlementsRaw,
    ReplaceEntitlementsRaw,
    ReplaceEntitlements0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
