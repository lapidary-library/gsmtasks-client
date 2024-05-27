# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.InvoiceAccount.schema
import gsmtasks.components.schemas.InvoiceItem.schema
import lapidary.runtime
import uuid


class Invoice(lapidary.runtime.ModelBase):
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
        typing.Union[None, gsmtasks.components.schemas.InvoiceAccount.schema.InvoiceAccount],
        pydantic.Field(
            alias='account',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    billing_method: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_method',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    period: typing.Annotated[
        typing.Union[None, list[datetime.date]],
        pydantic.Field(
            alias='period',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    total_no_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='total_no_vat',
            direction=lapidary.runtime.ParamDirection.read,
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    total_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='total_vat',
            direction=lapidary.runtime.ParamDirection.read,
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    total_with_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='total_with_vat',
            direction=lapidary.runtime.ParamDirection.read,
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    currency: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='currency',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    vat: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='vat',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    paid_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='paid_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    items: typing.Annotated[
        typing.Union[None, list[gsmtasks.components.schemas.InvoiceItem.schema.InvoiceItem]],
        pydantic.Field(
            alias='items',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    pricing: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='pricing',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    confirmed_by: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='confirmed_by',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    confirmed_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='confirmed_at',
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

    due_date: typing.Annotated[
        typing.Union[None, datetime.date],
        pydantic.Field(
            alias='due_date',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )