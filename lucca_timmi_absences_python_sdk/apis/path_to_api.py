import typing_extensions

from lucca_timmi_absences_python_sdk.paths import PathValues
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_leaves import ApiV3Leaves
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_leaves_leave_id import ApiV3LeavesLeaveId
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_leave_requests import ApiV3LeaveRequests
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_leave_requests_leave_request_id import ApiV3LeaveRequestsLeaveRequestId
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_leave_requests_leave_request_id_approvals import ApiV3LeaveRequestsLeaveRequestIdApprovals
from lucca_timmi_absences_python_sdk.apis.paths.figgo_api_public_services_v1_0_leave_entitlements_import import FiggoApiPublicServicesV10LeaveEntitlementsImport
from lucca_timmi_absences_python_sdk.apis.paths.timmi_absences_api_public_services_v1_0_leave_entitlements_import import TimmiAbsencesApiPublicServicesV10LeaveEntitlementsImport
from lucca_timmi_absences_python_sdk.apis.paths.figgo_api_public_services_v1_0_leave_entitlements_replace import FiggoApiPublicServicesV10LeaveEntitlementsReplace
from lucca_timmi_absences_python_sdk.apis.paths.timmi_absences_api_public_services_v1_0_leave_entitlements_replace import TimmiAbsencesApiPublicServicesV10LeaveEntitlementsReplace
from lucca_timmi_absences_python_sdk.apis.paths.api_v3_services_import_leave_periods import ApiV3ServicesImportLeavePeriods
from lucca_timmi_absences_python_sdk.apis.paths.timmi_absences_api_imports_v1_0_leave_periods import TimmiAbsencesApiImportsV10LeavePeriods
from lucca_timmi_absences_python_sdk.apis.paths.timmi_absences_api_imports_v1_0_leave_periods_summary_id_progress import TimmiAbsencesApiImportsV10LeavePeriodsSummaryIdProgress

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V3_LEAVES: ApiV3Leaves,
        PathValues.API_V3_LEAVES_LEAVE_ID: ApiV3LeavesLeaveId,
        PathValues.API_V3_LEAVE_REQUESTS: ApiV3LeaveRequests,
        PathValues.API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID: ApiV3LeaveRequestsLeaveRequestId,
        PathValues.API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID_APPROVALS: ApiV3LeaveRequestsLeaveRequestIdApprovals,
        PathValues.FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT: FiggoApiPublicServicesV10LeaveEntitlementsImport,
        PathValues.TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT: TimmiAbsencesApiPublicServicesV10LeaveEntitlementsImport,
        PathValues.FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE: FiggoApiPublicServicesV10LeaveEntitlementsReplace,
        PathValues.TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE: TimmiAbsencesApiPublicServicesV10LeaveEntitlementsReplace,
        PathValues.API_V3_SERVICES_IMPORT_LEAVE_PERIODS: ApiV3ServicesImportLeavePeriods,
        PathValues.TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS: TimmiAbsencesApiImportsV10LeavePeriods,
        PathValues.TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS_SUMMARY_ID_PROGRESS: TimmiAbsencesApiImportsV10LeavePeriodsSummaryIdProgress,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V3_LEAVES: ApiV3Leaves,
        PathValues.API_V3_LEAVES_LEAVE_ID: ApiV3LeavesLeaveId,
        PathValues.API_V3_LEAVE_REQUESTS: ApiV3LeaveRequests,
        PathValues.API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID: ApiV3LeaveRequestsLeaveRequestId,
        PathValues.API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID_APPROVALS: ApiV3LeaveRequestsLeaveRequestIdApprovals,
        PathValues.FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT: FiggoApiPublicServicesV10LeaveEntitlementsImport,
        PathValues.TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT: TimmiAbsencesApiPublicServicesV10LeaveEntitlementsImport,
        PathValues.FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE: FiggoApiPublicServicesV10LeaveEntitlementsReplace,
        PathValues.TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE: TimmiAbsencesApiPublicServicesV10LeaveEntitlementsReplace,
        PathValues.API_V3_SERVICES_IMPORT_LEAVE_PERIODS: ApiV3ServicesImportLeavePeriods,
        PathValues.TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS: TimmiAbsencesApiImportsV10LeavePeriods,
        PathValues.TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS_SUMMARY_ID_PROGRESS: TimmiAbsencesApiImportsV10LeavePeriodsSummaryIdProgress,
    }
)
