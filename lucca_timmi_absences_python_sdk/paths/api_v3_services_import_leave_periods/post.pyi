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

from lucca_timmi_absences_python_sdk.model.imports_absence_batch_create_response import ImportsAbsenceBatchCreateResponse as ImportsAbsenceBatchCreateResponseSchema

from lucca_timmi_absences_python_sdk.type.imports_absence_batch_create_response import ImportsAbsenceBatchCreateResponse

from ...api_client import Dictionary
from lucca_timmi_absences_python_sdk.pydantic.imports_absence_batch_create_response import ImportsAbsenceBatchCreateResponse as ImportsAbsenceBatchCreateResponsePydantic

# Query params


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
CreateSchema = schemas.BoolSchema
RecreditSchema = schemas.BoolSchema
OriginalFileNameSchema = schemas.StrSchema
SynchronizeSchema = schemas.BoolSchema
OverrideLeavesSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'type': typing.Union[TypeSchema, str, ],
        'originalFileName': typing.Union[OriginalFileNameSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'create': typing.Union[CreateSchema, bool, ],
        'recredit': typing.Union[RecreditSchema, bool, ],
        'synchronize': typing.Union[SynchronizeSchema, bool, ],
        'overrideLeaves': typing.Union[OverrideLeavesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    required=True,
    explode=True,
)
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
    required=True,
    explode=True,
)
request_query_synchronize = api_client.QueryParameter(
    name="synchronize",
    style=api_client.ParameterStyle.FORM,
    schema=SynchronizeSchema,
    explode=True,
)
request_query_override_leaves = api_client.QueryParameter(
    name="overrideLeaves",
    style=api_client.ParameterStyle.FORM,
    schema=OverrideLeavesSchema,
    explode=True,
)
# body param
SchemaForRequestBodyMultipartFormData = schemas.DictSchema


request_body_body = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
SchemaFor200ResponseBodyApplicationJson = ImportsAbsenceBatchCreateResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ImportsAbsenceBatchCreateResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ImportsAbsenceBatchCreateResponse


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

    def _absence_batch_create_mapped_args(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        args.body = _body
        if type is not None:
            _query_params["type"] = type
        if create is not None:
            _query_params["create"] = create
        if recredit is not None:
            _query_params["recredit"] = recredit
        if original_file_name is not None:
            _query_params["originalFileName"] = original_file_name
        if synchronize is not None:
            _query_params["synchronize"] = synchronize
        if override_leaves is not None:
            _query_params["overrideLeaves"] = override_leaves
        args.query = _query_params
        return args

    async def _aabsence_batch_create_oapg(
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
        Import leaves (deprecated)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_create,
            request_query_recredit,
            request_query_original_file_name,
            request_query_synchronize,
            request_query_override_leaves,
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
            path_template='/api/v3/services/importLeavePeriods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
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


    def _absence_batch_create_oapg(
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
        Import leaves (deprecated)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_create,
            request_query_recredit,
            request_query_original_file_name,
            request_query_synchronize,
            request_query_override_leaves,
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
            path_template='/api/v3/services/importLeavePeriods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
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


class AbsenceBatchCreateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def aabsence_batch_create(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._absence_batch_create_mapped_args(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
        )
        return await self._aabsence_batch_create_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def absence_batch_create(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._absence_batch_create_mapped_args(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
        )
        return self._absence_batch_create_oapg(
            body=args.body,
            query_params=args.query,
        )

class AbsenceBatchCreate(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def aabsence_batch_create(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ImportsAbsenceBatchCreateResponsePydantic:
        raw_response = await self.raw.aabsence_batch_create(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
            **kwargs,
        )
        if validate:
            return ImportsAbsenceBatchCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsAbsenceBatchCreateResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def absence_batch_create(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ImportsAbsenceBatchCreateResponsePydantic:
        raw_response = self.raw.absence_batch_create(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
        )
        if validate:
            return ImportsAbsenceBatchCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ImportsAbsenceBatchCreateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="imports")
    async def apost(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._absence_batch_create_mapped_args(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
        )
        return await self._aabsence_batch_create_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="imports")
    def post(
        self,
        type: str,
        original_file_name: str,
        create: typing.Optional[bool] = None,
        recredit: typing.Optional[bool] = None,
        synchronize: typing.Optional[bool] = None,
        override_leaves: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._absence_batch_create_mapped_args(
            type=type,
            original_file_name=original_file_name,
            create=create,
            recredit=recredit,
            synchronize=synchronize,
            override_leaves=override_leaves,
        )
        return self._absence_batch_create_oapg(
            body=args.body,
            query_params=args.query,
        )

