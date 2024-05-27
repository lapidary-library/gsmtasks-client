# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.NestedAddress.schema
import lapidary.runtime
import uuid


class Route(lapidary.runtime.ModelBase):
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

    code: typing.Annotated[
        str,
        pydantic.Field(
            alias='code',
            max_length=100,
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

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=100,
        )
    ] = None

    description: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='description',
        )
    ] = None

    assignee: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='assignee',
        )
    ] = None

    start_time: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='start_time',
        )
    ] = None

    start_address: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='start_address',
        )
    ] = None

    end_time: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='end_time',
        )
    ] = None

    end_address: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='end_address',
        )
    ] = None

    ObjectiveEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='ObjectiveEnum',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
