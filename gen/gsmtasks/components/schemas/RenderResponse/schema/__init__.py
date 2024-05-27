# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime


class RenderResponse(lapidary.runtime.ModelBase):
    task: typing.Annotated[
        str,
        pydantic.Field(
            alias='task',
        )
    ]

    sender: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='sender',
        )
    ] = None

    user: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='user',
        )
    ] = None

    event: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='event',
        )
    ] = None

    recipient: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='recipient',
        )
    ] = None

    emails: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='emails',
        )
    ] = None

    phones: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='phones',
        )
    ] = None

    app: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='app',
        )
    ] = None

    message: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='message',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )