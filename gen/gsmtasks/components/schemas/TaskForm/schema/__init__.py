# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class TaskForm(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID]

    url: typing.Union[None, str]

    task: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        )
    ]

    link: typing.Union[None, str]

    edit_url: typing.Annotated[
        str,
        pydantic.Field(
            max_length=2048,
        )
    ]

    open_in: typing.Union[None, str]

    created_at: typing.Union[None, datetime.datetime]

    updated_at: typing.Union[None, datetime.datetime]

    view_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

    pdf_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

    completed: typing.Union[None, bool] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
