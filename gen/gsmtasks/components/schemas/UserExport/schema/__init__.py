# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.TimeLocation.schema
import lapidary.runtime
import uuid


class UserExport(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID]

    display_name: typing.Union[None, str]

    email: str

    phone: typing.Union[None, str]

    TimeLocation: gsmtasks.components.schemas.TimeLocation.schema.TimeLocation

    first_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=30,
        )
    ] = None

    last_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=30,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
