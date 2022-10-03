from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.client
import gsmtasks.components.schemas.legacy_task
import gsmtasks.components.schemas.order
import gsmtasks.components.schemas.public_user


class OrderListScene(pydantic.BaseModel):
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

    assignees: typing.Annotated[
        list[
            gsmtasks.components.schemas.public_user.PublicUser,
        ],
        pydantic.Field(),
    ]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


OrderListScene.update_forward_refs()
