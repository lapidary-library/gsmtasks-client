# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class Export(lapidary.runtime.ModelBase):
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

    ExportModelEnum: typing.Annotated[
        str,
        pydantic.Field(
            alias='ExportModelEnum',
        )
    ]

    FormatEnum: typing.Annotated[
        str,
        pydantic.Field(
            alias='FormatEnum',
        )
    ]

    link: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='link',
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

    field_names: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='field_names',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
