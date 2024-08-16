# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.Document.properties.s3_response_headers.schema
import uuid


class Document(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    order: typing.Union[None, str] = None

    task: typing.Union[None, str] = None

    recurrence: typing.Union[None, str] = None

    file_upload: typing.Union[None, str] = None

    file: typing.Union[None, str] = None

    file_name: typing.Union[None, str] = None

    mimetype: typing.Union[None, str] = None

    thumbnail: typing.Union[None, str] = None

    description: typing.Union[None, str] = None

    s3_response_headers: typing.Union[None, gsmtasks.components.schemas.Document.properties.s3_response_headers.schema.s3_response_headers] = None

    created_by: typing.Union[None, str] = None

    source: typing.Union[None, str, typing.Any] = None

    visible_to_worker: typing.Union[None, bool] = None

    visible_to_client: typing.Union[None, bool] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )