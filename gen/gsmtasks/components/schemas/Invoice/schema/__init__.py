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
    id: typing.Union[None, uuid.UUID]

    url: typing.Union[None, str]

    account: typing.Union[None, gsmtasks.components.schemas.InvoiceAccount.schema.InvoiceAccount]

    billing_method: typing.Union[None, str]

    state: typing.Union[None, str]

    period: typing.Union[None, list[datetime.date]]

    total_no_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            regex='^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    total_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            regex='^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    total_with_vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            regex='^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    currency: typing.Union[None, str]

    vat: typing.Union[None, bool]

    paid_at: typing.Union[None, datetime.datetime]

    items: typing.Union[None, list[gsmtasks.components.schemas.InvoiceItem.schema.InvoiceItem]]

    pricing: typing.Union[None, uuid.UUID]

    confirmed_by: typing.Union[None, str]

    confirmed_at: typing.Union[None, datetime.datetime]

    created_at: typing.Union[None, datetime.datetime]

    updated_at: typing.Union[None, datetime.datetime]

    due_date: typing.Union[None, datetime.date] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
