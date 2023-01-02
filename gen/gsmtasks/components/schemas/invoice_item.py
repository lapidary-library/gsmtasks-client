# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import lapidary.runtime.absent
import uuid


class InvoiceItem(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    invoice: typing.Annotated[str, pydantic.Field()]

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        ),
    ]

    unit_price: typing.Annotated[
        str,
        pydantic.Field(
            regex=r"^-?\d{0,7}(?:\.\d{0,2})?$",
        ),
    ]

    quantity: typing.Annotated[
        str,
        pydantic.Field(
            regex=r"^-?\d{0,7}(?:\.\d{0,4})?$",
        ),
    ]

    unit: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=50,
        ),
    ] = lapidary.runtime.absent.ABSENT

    total: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
            regex=r"^-?\d{0,7}(?:\.\d{0,2})?$",
        ),
    ] = lapidary.runtime.absent.ABSENT

    created_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    updated_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


InvoiceItem.update_forward_refs()