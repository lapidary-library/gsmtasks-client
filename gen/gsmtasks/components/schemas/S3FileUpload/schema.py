# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.S3FileUpload.properties.s3_signature.schema
import uuid


class S3FileUpload(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    file: typing.Union[None, str] = None

    file_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    file_type: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    s3_signature: typing.Union[None, gsmtasks.components.schemas.S3FileUpload.properties.s3_signature.schema.s3_signature] = None

    created_by: typing.Union[None, str] = None

    source: typing.Union[None, str, typing.Any] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )