# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import gsmtasks.components.schemas.action_enum
import gsmtasks.components.schemas.location
import gsmtasks.components.schemas.task_command_state_enum
import gsmtasks.components.schemas.task_command_task_data
import lapidary.runtime.absent
import uuid


class TaskCommand(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    url: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    account: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    task: typing.Annotated[str, pydantic.Field()]

    external_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    time: typing.Annotated[datetime.datetime, pydantic.Field()]

    action: typing.Annotated[
        gsmtasks.components.schemas.action_enum.ActionEnum, pydantic.Field()
    ]

    user: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

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

    assignee: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_command_state_enum.TaskCommandStateEnum,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    error_message: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    task_data: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_command_task_data.TaskCommandTaskData,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    accepted_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    rejected_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
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


TaskCommand.update_forward_refs()
