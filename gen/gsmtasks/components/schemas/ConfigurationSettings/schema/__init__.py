# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.ConfigurationSettings.properties.task_command_queue_limit.schema
import lapidary.runtime


class ConfigurationSettings(lapidary.runtime.ModelBase):
    task_command_queue_limit: gsmtasks.components.schemas.ConfigurationSettings.properties.task_command_queue_limit.schema.task_command_queue_limit

    date_format: str

    time_format: str

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
