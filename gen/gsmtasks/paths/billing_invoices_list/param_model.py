# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import enum
import lapidary.runtime.absent


class BillingInvoicesListBillingMethod(enum.Enum):
    braintree = "braintree"
    invoice = "invoice"
    stripe = "stripe"


class BillingInvoicesListFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class BillingInvoicesListState(enum.Enum):
    draft = "draft"
    confirmed = "confirmed"
    overdue = "overdue"
    paid = "paid"
    cancelled = "cancelled"


class BillingInvoicesList(pydantic.BaseModel):
    q_account: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="account",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_billing_method: typing.Annotated[
        typing.Union[
            BillingInvoicesListBillingMethod,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="billing_method",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__date",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__date_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__gt",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__gt_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__gte",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__gte_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__lt",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__lt_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__lte",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_confirmed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="confirmed_at__lte_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__date",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__date_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__gt",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__gt_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__gte",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__gte_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__lt",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__lt_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__lte",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_created_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="created_at__lte_or_isnull",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_cursor: typing.Annotated[
        typing.Union[
            int,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="cursor",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            BillingInvoicesListFormat,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_ordering: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="ordering",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_page_size: typing.Annotated[
        typing.Union[
            int,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="page_size",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_state: typing.Annotated[
        typing.Union[
            BillingInvoicesListState,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="state",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


BillingInvoicesList.update_forward_refs()