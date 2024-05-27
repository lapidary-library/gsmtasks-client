# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.ConfigurationSettings.properties.task_command_queue_limit.schema
import lapidary.runtime


class ConfigurationSettings(lapidary.runtime.ModelBase):
    task_command_queue_limit: typing.Annotated[
        gsmtasks.components.schemas.ConfigurationSettings.properties.task_command_queue_limit.schema.task_command_queue_limit,
        pydantic.Field(
            alias='task_command_queue_limit',
        )
    ]

    date_format: typing.Annotated[
        str,
        pydantic.Field(
            alias='date_format',
        )
    ]

    time_format: typing.Annotated[
        str,
        pydantic.Field(
            alias='time_format',
        )
    ]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
