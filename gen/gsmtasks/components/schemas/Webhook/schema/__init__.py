# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.Webhook.properties.headers.schema
import lapidary.runtime
import uuid


class Webhook(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID]

    url: typing.Union[None, str]

    account: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    state: typing.Union[None, str]

    target: typing.Annotated[
        str,
        pydantic.Field(
            max_length=2048,
        )
    ]

    fail_message: typing.Union[None, str]

    activated_at: typing.Union[None, datetime.datetime]

    failed_at: typing.Union[None, datetime.datetime]

    created_at: typing.Union[None, datetime.datetime]

    updated_at: typing.Union[None, datetime.datetime]

    VersionEnum: typing.Union[None, str] = None

    headers: typing.Union[None, gsmtasks.components.schemas.Webhook.properties.headers.schema.headers] = None

    task_events: typing.Union[None, bool] = None

    document_events: typing.Union[None, bool] = None

    signature_events: typing.Union[None, bool] = None

    review_events: typing.Union[None, bool] = None

    notification_emails: typing.Union[None, list[str]] = None

    shared_secret: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=40,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
