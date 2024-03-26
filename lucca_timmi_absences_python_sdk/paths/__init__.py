# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_timmi_absences_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V3_LEAVES = "/api/v3/leaves"
    API_V3_LEAVES_LEAVE_ID = "/api/v3/leaves/{leaveId}"
    API_V3_LEAVE_REQUESTS = "/api/v3/leaveRequests"
    API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID = "/api/v3/leaveRequests/{leaveRequestId}"
    API_V3_LEAVE_REQUESTS_LEAVE_REQUEST_ID_APPROVALS = "/api/v3/leaveRequests/{leaveRequestId}/approvals"
    FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT = "/figgo/api/public/services/v1.0/leaveEntitlementsImport"
    TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_IMPORT = "/timmi-absences/api/public/services/v1.0/leaveEntitlementsImport"
    FIGGO_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE = "/figgo/api/public/services/v1.0/leaveEntitlementsReplace"
    TIMMIABSENCES_API_PUBLIC_SERVICES_V1_0_LEAVE_ENTITLEMENTS_REPLACE = "/timmi-absences/api/public/services/v1.0/leaveEntitlementsReplace"
    API_V3_SERVICES_IMPORT_LEAVE_PERIODS = "/api/v3/services/importLeavePeriods"
    TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS = "/timmi-absences/api/imports/v1.0/leavePeriods"
    TIMMIABSENCES_API_IMPORTS_V1_0_LEAVE_PERIODS_SUMMARY_ID_PROGRESS = "/timmi-absences/api/imports/v1.0/leavePeriods/{summaryId}/progress"
