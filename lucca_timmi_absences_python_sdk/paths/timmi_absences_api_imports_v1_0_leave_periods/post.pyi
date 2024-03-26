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

from lucca_timmi_absences_python_sdk.model.imports_create_absences_batch_request import ImportsCreateAbsencesBatchRequest as ImportsCreateAbsencesBatchRequestSchema
from lucca_timmi_absences_python_sdk.model.imports_create_absences_batch_response import ImportsCreateAbsencesBatchResponse as ImportsCreateAbsencesBatchResponseSchema
from lucca_timmi_absences_python_sdk.model.imports_create_absences_batch_request_files import ImportsCreateAbsencesBatchRequestFiles as ImportsCreateAbsencesBatchRequestFilesSchema

from lucca_timmi_absences_python_sdk.type.imports_create_absences_batch_request import ImportsCreateAbsencesBatchRequest
from lucca_timmi_absences_python_sdk.type.imports_create_absences_batch_response import ImportsCreateAbsencesBatchResponse
from lucca_timmi_absences_python_sdk.type.imports_create_absences_batch_request_files import ImportsCreateAbsencesBatchRequestFiles

from ...api_client import Dictionary
from lucca_timmi_absences_python_sdk.pydantic.imports_create_absences_batch_response import ImportsCreateAbsencesBatchResponse as ImportsCreateAbsencesBatchResponsePydantic
from lucca_timmi_absences_python_sdk.pydantic.imports_create_absences_batch_request_files import ImportsCreateAbsencesBatchRequestFiles as ImportsCreateAbsencesBatchRequestFilesPydantic
from lucca_timmi_absences_python_sdk.pydantic.imports_create_absences_batch_request import ImportsCreateAbsencesBatchRequest as ImportsCreateAbsencesBatchRequestPydantic

# Query params
CreateSchema = schemas.BoolSchema
RecreditSchema = schemas.BoolSchema
OriginalFileNameSchema = schemas.StrSchema
SynchronizeSchema = schemas.BoolSchema
ModelAsyncSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'create': typing.Union[CreateSchema, bool, ],
        'recredit': typing.Union[RecreditSchema, bool, ],
        'originalFileName': typing.Union[OriginalFileNameSchema, str, ],
        'synchronize': typing.Union[SynchronizeSchema, bool, ],
        'async': typing.Union[ModelAsyncSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_create = api_client.QueryParameter(
    name="create",
    style=api_client.ParameterStyle.FORM,
    schema=CreateSchema,
    explode=True,
)
request_query_recredit = api_client.QueryParameter(
    name="recredit",
    style=api_client.ParameterStyle.FORM,
    schema=RecreditSchema,
    explode=True,
)
request_query_original_file_name = api_client.QueryParameter(
    name="originalFileName",
    style=api_client.ParameterStyle.FORM,
    schema=OriginalFileNameSchema,
    explode=True,
)
request_query_synchronize = api_client.QueryParameter(
    name="synchronize",
    style=api_client.ParameterStyle.FORM,
    schema=SynchronizeSchema,
    explode=True,
)
request_query__async = api_client.QueryParameter(
    name="async",
    style=api_client.ParameterStyle.FORM,
    schema=ModelAsyncSchema,
    explode=True,
)
# body param
SchemaForRequestBodyMultipartFormData = ImportsCreateAbsencesBatchRequestSchema


request_body_imports_create_absences_batch_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
SchemaFor200ResponseBodyApplicationJson = ImportsCreateAbsencesBatchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ImportsCreateAbsencesBatchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ImportsCreateAbsencesBatchResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_absences_batch_mapped_args(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if files is not None:
            _body["files"] = files
        args.body = _body
        if create is not None:
            _query_params["create"] = create
        if recredit is not None:
            _query_params["recredit"] = recredit
        if original_file_name is not None:
            _query_params["originalFileName"] = original_file_name
        if synchronize is not None:
            _query_params["synchronize"] = synchronize
        if _async is not None:
            _query_params["async"] = _async
        args.query = _query_params
        return args

    async def _acreate_absences_batch_oapg(
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
        Import leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_create,
            request_query_recredit,
            request_query_original_file_name,
            request_query_synchronize,
            request_query__async,
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
            path_template='/timmi-absences/api/imports/v1.0/leavePeriods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_imports_create_absences_batch_request.serialize(body, content_type)
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


    def _create_absences_batch_oapg(
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
        Import leaves
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_create,
            request_query_recredit,
            request_query_original_file_name,
            request_query_synchronize,
            request_query__async,
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
            path_template='/timmi-absences/api/imports/v1.0/leavePeriods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_imports_create_absences_batch_request.serialize(body, content_type)
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


class CreateAbsencesBatchRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_absences_batch(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_absences_batch_mapped_args(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
        )
        return await self._acreate_absences_batch_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_absences_batch(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_absences_batch_mapped_args(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
        )
        return self._create_absences_batch_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreateAbsencesBatch(BaseApi):

    async def acreate_absences_batch(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
        validate: bool = False,
        **kwargs,
    ) -> ImportsCreateAbsencesBatchResponsePydantic:
        raw_response = await self.raw.acreate_absences_batch(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
            **kwargs,
        )
        if validate:
            return ImportsCreateAbsencesBatchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsCreateAbsencesBatchResponsePydantic, raw_response.body)
    
    
    def create_absences_batch(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
        validate: bool = False,
    ) -> ImportsCreateAbsencesBatchResponsePydantic:
        raw_response = self.raw.create_absences_batch(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
        )
        if validate:
            return ImportsCreateAbsencesBatchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsCreateAbsencesBatchResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_absences_batch_mapped_args(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
        )
        return await self._acreate_absences_batch_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        original_file_name: typing.Optional[str] = None,
        synchronize: typing.Optional[bool] = None,
        _async: typing.Optional[bool] = None,
        files: typing.Optional[ImportsCreateAbsencesBatchRequestFiles] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_absences_batch_mapped_args(
            create=create,
            recredit=recredit,
            original_file_name=original_file_name,
            synchronize=synchronize,
            _async=_async,
            files=files,
        )
        return self._create_absences_batch_oapg(
            body=args.body,
            query_params=args.query,
        )

