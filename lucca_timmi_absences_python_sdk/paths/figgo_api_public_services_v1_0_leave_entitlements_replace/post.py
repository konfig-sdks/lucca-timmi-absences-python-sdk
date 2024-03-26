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

from lucca_timmi_absences_python_sdk.model.imports_entitlements_batch_import_response import ImportsEntitlementsBatchImportResponse as ImportsEntitlementsBatchImportResponseSchema
from lucca_timmi_absences_python_sdk.model.imports_replace_entitlements_request import ImportsReplaceEntitlementsRequest as ImportsReplaceEntitlementsRequestSchema

from lucca_timmi_absences_python_sdk.type.imports_replace_entitlements_request import ImportsReplaceEntitlementsRequest
from lucca_timmi_absences_python_sdk.type.imports_entitlements_batch_import_response import ImportsEntitlementsBatchImportResponse

from ...api_client import Dictionary
from lucca_timmi_absences_python_sdk.pydantic.imports_replace_entitlements_request import ImportsReplaceEntitlementsRequest as ImportsReplaceEntitlementsRequestPydantic
from lucca_timmi_absences_python_sdk.pydantic.imports_entitlements_batch_import_response import ImportsEntitlementsBatchImportResponse as ImportsEntitlementsBatchImportResponsePydantic

from . import path

# Query params
StrictSchema = schemas.BoolSchema
SimulateSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'strict': typing.Union[StrictSchema, bool, ],
        'simulate': typing.Union[SimulateSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_strict = api_client.QueryParameter(
    name="strict",
    style=api_client.ParameterStyle.FORM,
    schema=StrictSchema,
    explode=True,
)
request_query_simulate = api_client.QueryParameter(
    name="simulate",
    style=api_client.ParameterStyle.FORM,
    schema=SimulateSchema,
    explode=True,
)
# body param
SchemaForRequestBodyMultipartFormData = ImportsReplaceEntitlementsRequestSchema


request_body_imports_replace_entitlements_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = ImportsEntitlementsBatchImportResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ImportsEntitlementsBatchImportResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ImportsEntitlementsBatchImportResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _replace_entitlements_mapped_args(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if file is not None:
            _body["File"] = file
        if description is not None:
            _body["Description"] = description
        if reference_date is not None:
            _body["ReferenceDate"] = reference_date
        if entry_types is not None:
            _body["EntryTypes"] = entry_types
        args.body = _body
        if strict is not None:
            _query_params["strict"] = strict
        if simulate is not None:
            _query_params["simulate"] = simulate
        args.query = _query_params
        return args

    async def _areplace_entitlements_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Replace entitlements (deprecated)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_strict,
            request_query_simulate,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/figgo/api/public/services/v1.0/leaveEntitlementsReplace',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_imports_replace_entitlements_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _replace_entitlements_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Replace entitlements (deprecated)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_strict,
            request_query_simulate,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/figgo/api/public/services/v1.0/leaveEntitlementsReplace',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_imports_replace_entitlements_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class ReplaceEntitlementsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def areplace_entitlements(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._replace_entitlements_mapped_args(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
        )
        return await self._areplace_entitlements_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def replace_entitlements(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._replace_entitlements_mapped_args(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
        )
        return self._replace_entitlements_oapg(
            body=args.body,
            query_params=args.query,
        )

class ReplaceEntitlements(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def areplace_entitlements(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ImportsEntitlementsBatchImportResponsePydantic:
        raw_response = await self.raw.areplace_entitlements(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
            **kwargs,
        )
        if validate:
            return ImportsEntitlementsBatchImportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsEntitlementsBatchImportResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def replace_entitlements(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ImportsEntitlementsBatchImportResponsePydantic:
        raw_response = self.raw.replace_entitlements(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
        )
        if validate:
            return ImportsEntitlementsBatchImportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsEntitlementsBatchImportResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def apost(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._replace_entitlements_mapped_args(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
        )
        return await self._areplace_entitlements_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def post(
        self,
        strict: typing.Optional[bool] = None,
        simulate: typing.Optional[bool] = None,
        file: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        reference_date: typing.Optional[datetime] = None,
        entry_types: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._replace_entitlements_mapped_args(
            strict=strict,
            simulate=simulate,
            file=file,
            description=description,
            reference_date=reference_date,
            entry_types=entry_types,
        )
        return self._replace_entitlements_oapg(
            body=args.body,
            query_params=args.query,
        )

