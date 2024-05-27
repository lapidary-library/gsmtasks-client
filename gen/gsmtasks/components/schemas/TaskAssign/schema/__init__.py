# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.Location.schema
import lapidary.runtime


class TaskAssign(lapidary.runtime.ModelBase):
    assignee: typing.Annotated[
        str,
        pydantic.Field(
            alias='assignee',
        )
    ]

    notes: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='notes',
        )
    ] = None

    location: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.Location.schema.Location],
        pydantic.Field(
            alias='location',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
