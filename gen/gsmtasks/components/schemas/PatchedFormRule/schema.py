# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import gsmtasks.components.schemas.PatchedFormRule.properties.rules.schema
import uuid


class PatchedFormRule(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    is_active: typing.Union[None, bool] = None

    name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=50,
        )
    ] = None

    edit_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

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

    rules: typing.Union[None, gsmtasks.components.schemas.PatchedFormRule.properties.rules.schema.rules] = None

    open_in: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
