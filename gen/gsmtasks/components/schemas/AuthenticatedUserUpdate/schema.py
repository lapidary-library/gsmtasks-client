# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import gsmtasks.components.schemas.NestedAddress.schema
import uuid


class AuthenticatedUserUpdate(lapidary.runtime.ModelBase):
    email: str

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

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

    display_name: typing.Union[None, str] = None

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=128,
        )
    ] = None

    address: typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
