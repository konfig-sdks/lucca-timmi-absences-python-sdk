# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id_approvals.post import ApproveDenyRaw
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id.delete import CancelRequestRaw
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id.get import GetByIdRaw
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests.get import ListRaw


class LeaveRequestsApiRaw(
    ApproveDenyRaw,
    CancelRequestRaw,
    GetByIdRaw,
    ListRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass