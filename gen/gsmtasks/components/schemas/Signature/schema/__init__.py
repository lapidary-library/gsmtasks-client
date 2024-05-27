# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.Location.schema
import gsmtasks.components.schemas.NestedContact.schema
import gsmtasks.components.schemas.Signature.properties.s3_response_headers.schema
import lapidary.runtime
import uuid


class Signature(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    task: typing.Annotated[
        str,
        pydantic.Field(
            alias='task',
        )
    ]

    file_upload: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='file_upload',
            direction=lapidary.runtime.ParamDirection.write,
        )
    ]

    file: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='file',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    file_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='file_name',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    mimetype: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='mimetype',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    thumbnail: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='thumbnail',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    NestedContact: typing.Annotated[
        gsmtasks.components.schemas.NestedContact.schema.NestedContact,
        pydantic.Field(
            alias='NestedContact',
        )
    ]

    created_by: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='created_by',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='created_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    updated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='updated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='account',
        )
    ] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=100,
        )
    ] = None

    documents: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='documents',
        )
    ] = None

    location: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.Location.schema.Location],
        pydantic.Field(
            alias='location',
        )
    ] = None

    s3_response_headers: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.Signature.properties.s3_response_headers.schema.s3_response_headers],
        pydantic.Field(
            alias='s3_response_headers',
            direction=lapidary.runtime.ParamDirection.write,
        )
    ] = None

    source: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='source',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )