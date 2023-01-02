# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import gsmtasks.components.schemas.location
import lapidary.runtime.absent


class TaskAction(pydantic.BaseModel):
    notes: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    location: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.location.Location,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


TaskAction.update_forward_refs()
