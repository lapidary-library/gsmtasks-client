# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.Client.properties.contact_addresses.items.schema
import uuid


class Client(lapidary.runtime.ModelBase):
    account: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        )
    ]

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    slug: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            pattern=r'^[-a-zA-Z0-9_]+$',
        )
    ] = None

    archived: typing.Union[None, bool] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    contact_addresses: typing.Union[None, list[gsmtasks.components.schemas.Client.properties.contact_addresses.items.schema.items]] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )