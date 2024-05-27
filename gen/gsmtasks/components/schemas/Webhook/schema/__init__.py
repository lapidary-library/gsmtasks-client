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

    account: typing.Annotated[
        str,
        pydantic.Field(
            alias='account',
        )
    ]

    name: typing.Annotated[
        str,
        pydantic.Field(
            alias='name',
            max_length=100,
        )
    ]

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    target: typing.Annotated[
        str,
        pydantic.Field(
            alias='target',
            max_length=2048,
        )
    ]

    fail_message: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='fail_message',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    activated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='activated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    failed_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='failed_at',
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

    VersionEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='VersionEnum',
        )
    ] = None

    headers: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.Webhook.properties.headers.schema.headers],
        pydantic.Field(
            alias='headers',
        )
    ] = None

    task_events: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='task_events',
        )
    ] = None

    document_events: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='document_events',
        )
    ] = None

    signature_events: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='signature_events',
        )
    ] = None

    review_events: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='review_events',
        )
    ] = None

    notification_emails: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='notification_emails',
        )
    ] = None

    shared_secret: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='shared_secret',
            max_length=40,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
