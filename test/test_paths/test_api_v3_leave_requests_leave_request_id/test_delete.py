# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest
from unittest.mock import patch

import urllib3

import lucca_timmi_absences_python_sdk
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests_leave_request_id import delete
from lucca_timmi_absences_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3LeaveRequestsLeaveRequestId(ApiTestMixin, unittest.TestCase):
    """
    ApiV3LeaveRequestsLeaveRequestId unit test stubs
        Request to cancel a leave request
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
