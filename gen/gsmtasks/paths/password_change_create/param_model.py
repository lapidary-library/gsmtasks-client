# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum
import lapidary.runtime.absent


class PasswordChangeCreateFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class PasswordChangeCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            PasswordChangeCreateFormat,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


PasswordChangeCreate.update_forward_refs()
