# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum
import lapidary.runtime.absent
import uuid


class AccountsWorkersCreateFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class AccountsWorkersCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            AccountsWorkersCreateFormat,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    p_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            alias="id",
            in_=lapidary.runtime.ParamPlacement.path,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountsWorkersCreate.update_forward_refs()
