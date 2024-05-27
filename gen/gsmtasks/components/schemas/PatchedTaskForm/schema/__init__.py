# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class PatchedTaskForm(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    task: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='task',
        )
    ] = None

    name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='name',
            max_length=50,
        )
    ] = None

    link: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='link',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    edit_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='edit_url',
            max_length=2048,
        )
    ] = None

    view_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='view_url',
            max_length=2048,
        )
    ] = None

    pdf_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='pdf_url',
            max_length=2048,
        )
    ] = None

    open_in: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='open_in',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    completed: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='completed',
        )
    ] = None

    created_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='created_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    updated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='updated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
