# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class SMS(lapidary.runtime.ModelBase):
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

    sender: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='sender',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    phone: typing.Annotated[
        str,
        pydantic.Field(
            alias='phone',
            max_length=128,
        )
    ]

    sent_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='sent_at',
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

    received_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='received_at',
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
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=34,
        )
    ] = None

    alphanumeric_sender_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='alphanumeric_sender_id',
            max_length=20,
        )
    ] = None

    message: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='message',
        )
    ] = None

    segments_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='segments_count',
            ge=-2147483648.0,
            le=2147483647.0,
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
