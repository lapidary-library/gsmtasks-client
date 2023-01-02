# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import lapidary.runtime.absent
import uuid


class InvoiceAccount(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    slug: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
            regex=r"^[-a-zA-Z0-9_]+$",
        ),
    ] = lapidary.runtime.absent.ABSENT

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    registry_code: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary.runtime.absent.ABSENT

    vatin: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary.runtime.absent.ABSENT

    billing_reference: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary.runtime.absent.ABSENT

    billing_email: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=254,
        ),
    ] = lapidary.runtime.absent.ABSENT

    billing_vat: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


InvoiceAccount.update_forward_refs()
