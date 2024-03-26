import typing_extensions

from lucca_timmi_absences_python_sdk.apis.tags import TagValues
from lucca_timmi_absences_python_sdk.apis.tags.imports_api import ImportsApi
from lucca_timmi_absences_python_sdk.apis.tags.leave_requests_api import LeaveRequestsApi
from lucca_timmi_absences_python_sdk.apis.tags.leaves_api import LeavesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.IMPORTS: ImportsApi,
        TagValues.LEAVE_REQUESTS: LeaveRequestsApi,
        TagValues.LEAVES: LeavesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.IMPORTS: ImportsApi,
        TagValues.LEAVE_REQUESTS: LeaveRequestsApi,
        TagValues.LEAVES: LeavesApi,
    }
)
