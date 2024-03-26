# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id_approvals.post import ApproveDeny
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id.delete import CancelRequest
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id.get import GetById
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests.get import List
from lucca_timmi_absences_python_sdk.apis.tags.leave_requests_api_raw import LeaveRequestsApiRaw


class LeaveRequestsApi(
    ApproveDeny,
    CancelRequest,
    GetById,
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LeaveRequestsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LeaveRequestsApiRaw(api_client)