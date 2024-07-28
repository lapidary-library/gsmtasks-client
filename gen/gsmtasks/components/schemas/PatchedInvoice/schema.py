# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import decimal
import gsmtasks.components.schemas.InvoiceAccount.schema
import gsmtasks.components.schemas.InvoiceItem.schema
import uuid


class PatchedInvoice(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, gsmtasks.components.schemas.InvoiceAccount.schema.InvoiceAccount] = None

    billing_method: typing.Union[None, str] = None

    state: typing.Union[None, str] = None

    period: typing.Union[None, list[datetime.date]] = None

    total_no_vat: typing.Union[None, decimal.Decimal] = None

    total_vat: typing.Union[None, decimal.Decimal] = None

    total_with_vat: typing.Union[None, decimal.Decimal] = None

    currency: typing.Union[None, str] = None

    vat: typing.Union[None, bool] = None

    due_date: typing.Union[None, datetime.date] = None

    paid_at: typing.Union[None, datetime.datetime] = None

    items: typing.Union[None, list[gsmtasks.components.schemas.InvoiceItem.schema.InvoiceItem]] = None

    pricing: typing.Union[None, uuid.UUID] = None

    confirmed_by: typing.Union[None, str] = None

    confirmed_at: typing.Union[None, datetime.datetime] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
