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
from lucca_timmi_absences_python_sdk.paths.api_v3_leave_requests import get
from lucca_timmi_absences_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3LeaveRequests(ApiTestMixin, unittest.TestCase):
    """
    ApiV3LeaveRequests unit test stubs
        List leave requests
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
