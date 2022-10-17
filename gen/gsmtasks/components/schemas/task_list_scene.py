from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.client
import gsmtasks.components.schemas.legacy_task
import gsmtasks.components.schemas.order
import gsmtasks.components.schemas.public_user
import gsmtasks.components.schemas.task_event
import gsmtasks.components.schemas.task_metadata
import lapidary_base.absent


class TaskListScene(pydantic.BaseModel):
    clients: typing.Annotated[
        list[
            gsmtasks.components.schemas.client.Client,
        ],
        pydantic.Field(),
    ]

    orders: typing.Annotated[
        list[
            gsmtasks.components.schemas.order.Order,
        ],
        pydantic.Field(),
    ]

    tasks: typing.Annotated[
        list[
            gsmtasks.components.schemas.legacy_task.LegacyTask,
        ],
        pydantic.Field(),
    ]

    task_metadatas: typing.Annotated[
        list[
            gsmtasks.components.schemas.task_metadata.TaskMetadata,
        ],
        pydantic.Field(),
    ]

    task_events_with_notes: typing.Annotated[
        list[
            gsmtasks.components.schemas.task_event.TaskEvent,
        ],
        pydantic.Field(),
    ]

    users: typing.Annotated[
        list[
            gsmtasks.components.schemas.public_user.PublicUser,
        ],
        pydantic.Field(),
    ]

    updated_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


TaskListScene.update_forward_refs()
