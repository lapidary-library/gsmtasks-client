from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.location
import lapidary_base.absent
import uuid


class WorkerTrack(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    track: typing.Annotated[
        gsmtasks.components.schemas.location.Location, pydantic.Field()
    ]

    user: typing.Annotated[uuid.UUID, pydantic.Field()]

    start_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    end_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


WorkerTrack.update_forward_refs()
