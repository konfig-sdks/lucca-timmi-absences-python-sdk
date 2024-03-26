# coding: utf-8

"""
    Timmi Absences API

    Welcome on the documentation for Timmi Absences API.

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lucca_timmi_absences_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lucca_timmi_absences_python_sdk.api_response import AsyncGeneratorResponse
from lucca_timmi_absences_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_timmi_absences_python_sdk import schemas  # noqa: F401

from lucca_timmi_absences_python_sdk.model.leaves_get_approved_list_response import LeavesGetApprovedListResponse as LeavesGetApprovedListResponseSchema

from lucca_timmi_absences_python_sdk.type.leaves_get_approved_list_response import LeavesGetApprovedListResponse

from ...api_client import Dictionary
from lucca_timmi_absences_python_sdk.pydantic.leaves_get_approved_list_response import LeavesGetApprovedListResponse as LeavesGetApprovedListResponsePydantic

from . import path

# Query params
PagingSchema = schemas.StrSchema
LeaveAccountIdSchema = schemas.StrSchema


class LeavePeriodOwnerIdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LeavePeriodOwnerIdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
DateSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'paging': typing.Union[PagingSchema, str, ],
        'leavePeriod.ownerId': typing.Union[LeavePeriodOwnerIdSchema, list, tuple, ],
        'date': typing.Union[DateSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'leaveAccountId': typing.Union[LeaveAccountIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_paging = api_client.QueryParameter(
    name="paging",
    style=api_client.ParameterStyle.FORM,
    schema=PagingSchema,
    required=True,
    explode=True,
)
request_query_leave_account_id = api_client.QueryParameter(
    name="leaveAccountId",
    style=api_client.ParameterStyle.FORM,
    schema=LeaveAccountIdSchema,
    explode=True,
)
request_query_leave_period_owner_id = api_client.QueryParameter(
    name="leavePeriod.ownerId",
    style=api_client.ParameterStyle.FORM,
    schema=LeavePeriodOwnerIdSchema,
    required=True,
    explode=True,
)
request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    required=True,
    explode=True,
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = LeavesGetApprovedListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LeavesGetApprovedListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LeavesGetApprovedListResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_approved_list_mapped_args(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if paging is not None:
            _query_params["paging"] = paging
        if leave_account_id is not None:
            _query_params["leaveAccountId"] = leave_account_id
        if leave_period_owner_id is not None:
            _query_params["leavePeriod.ownerId"] = leave_period_owner_id
        if date is not None:
            _query_params["date"] = date
        args.query = _query_params
        return args

    async def _aget_approved_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_paging,
            request_query_leave_account_id,
            request_query_leave_period_owner_id,
            request_query_date,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/leaves',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_approved_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_paging,
            request_query_leave_account_id,
            request_query_leave_period_owner_id,
            request_query_date,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/leaves',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetApprovedListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_approved_list(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_approved_list_mapped_args(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
        )
        return await self._aget_approved_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_approved_list(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_approved_list_mapped_args(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
        )
        return self._get_approved_list_oapg(
            query_params=args.query,
        )

class GetApprovedList(BaseApi):

    async def aget_approved_list(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LeavesGetApprovedListResponsePydantic:
        raw_response = await self.raw.aget_approved_list(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
            **kwargs,
        )
        if validate:
            return LeavesGetApprovedListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeavesGetApprovedListResponsePydantic, raw_response.body)
    
    
    def get_approved_list(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LeavesGetApprovedListResponsePydantic:
        raw_response = self.raw.get_approved_list(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
        )
        if validate:
            return LeavesGetApprovedListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LeavesGetApprovedListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_approved_list_mapped_args(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
        )
        return await self._aget_approved_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        paging: str,
        leave_period_owner_id: typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
        date: str,
        leave_account_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_approved_list_mapped_args(
            paging=paging,
            leave_period_owner_id=leave_period_owner_id,
            date=date,
            leave_account_id=leave_account_id,
        )
        return self._get_approved_list_oapg(
            query_params=args.query,
        )

