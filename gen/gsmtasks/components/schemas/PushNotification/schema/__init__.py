# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class PushNotification(lapidary.runtime.ModelBase):
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

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    notification: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='notification',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    recipient: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='recipient',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    task: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='task',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    message: typing.Annotated[
        str,
        pydantic.Field(
            alias='message',
        )
    ]

    pending_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='pending_at',
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

    sent_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='sent_at',
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

    external_id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='external_id',
        )
    ] = None

    event: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='event',
        )
    ] = None

    subject: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='subject',
        )
    ] = None

    error: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='error',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )