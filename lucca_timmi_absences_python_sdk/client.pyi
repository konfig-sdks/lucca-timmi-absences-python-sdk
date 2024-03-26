# coding: utf-8
"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import typing
import inspect
from datetime import date, datetime
from lucca_timmi_absences_python_sdk.client_custom import ClientCustom
from lucca_timmi_absences_python_sdk.configuration import Configuration
from lucca_timmi_absences_python_sdk.api_client import ApiClient
from lucca_timmi_absences_python_sdk.type_util import copy_signature
from lucca_timmi_absences_python_sdk.apis.tags.imports_api import ImportsApi
from lucca_timmi_absences_python_sdk.apis.tags.leave_requests_api import LeaveRequestsApi
from lucca_timmi_absences_python_sdk.apis.tags.leaves_api import LeavesApi



class LuccaTimmiAbsences(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.imports: ImportsApi = ImportsApi(api_client)
        self.leave_requests: LeaveRequestsApi = LeaveRequestsApi(api_client)
        self.leaves: LeavesApi = LeavesApi(api_client)
