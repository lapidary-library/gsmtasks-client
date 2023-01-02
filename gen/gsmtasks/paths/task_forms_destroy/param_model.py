# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum
import lapidary.runtime.absent
import uuid


class TaskFormsDestroyFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class TaskFormsDestroy(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            TaskFormsDestroyFormat,
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


TaskFormsDestroy.update_forward_refs()
