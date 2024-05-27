# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime
import uuid


class RegistrationUser(lapidary.runtime.ModelBase):
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

    name: typing.Annotated[
        str,
        pydantic.Field(
            alias='name',
            max_length=30,
        )
    ]

    email: typing.Annotated[
        str,
        pydantic.Field(
            alias='email',
            max_length=254,
        )
    ]

    password: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='password',
            direction=lapidary.runtime.ParamDirection.write,
            max_length=100,
            min_length=6,
        )
    ]

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='phone',
            max_length=128,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
