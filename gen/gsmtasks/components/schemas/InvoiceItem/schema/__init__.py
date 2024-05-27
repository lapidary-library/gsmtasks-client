# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class InvoiceItem(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    invoice: typing.Annotated[
        str,
        pydantic.Field(
            alias='invoice',
        )
    ]

    name: typing.Annotated[
        str,
        pydantic.Field(
            alias='name',
            max_length=200,
        )
    ]

    unit_price: typing.Annotated[
        str,
        pydantic.Field(
            alias='unit_price',
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    quantity: typing.Annotated[
        str,
        pydantic.Field(
            alias='quantity',
            regex=r'^-?\d{0,7}(?:\.\d{0,4})?$',
        )
    ]

    total: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='total',
            direction=lapidary.runtime.ParamDirection.read,
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
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

    unit: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='unit',
            max_length=50,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
