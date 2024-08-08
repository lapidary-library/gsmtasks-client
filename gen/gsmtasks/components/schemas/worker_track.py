# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import gsmtasks.components.schemas.location
import lapidary.runtime.absent
import uuid


class WorkerTrack(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    track: typing.Annotated[
        gsmtasks.components.schemas.location.Location, pydantic.Field()
    ]

    user: typing.Annotated[uuid.UUID, pydantic.Field()]

    start_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    end_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


WorkerTrack.update_forward_refs()