# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class PatchedMetafield(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    ordering: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0,
            le=2147483647,
        )
    ] = None

    namespace: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
            pattern=r'^[a-z0-9_]+$',
        )
    ] = None

    key: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
            pattern=r'^[a-z0-9_]+$',
        )
    ] = None

    field_name: typing.Union[None, str] = None

    value_type: typing.Union[None, str] = None

    label: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=40,
        )
    ] = None

    choices: typing.Union[None, list[str]] = None

    choices_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

    is_editable: typing.Union[None, bool] = None

    is_editable_assignee: typing.Union[None, bool] = None

    is_required: typing.Union[None, bool] = None

    is_persistent: typing.Union[None, bool] = None

    is_cloned: typing.Union[None, bool] = None

    is_searchable: typing.Union[None, bool] = None

    show_in_list_view: typing.Union[None, bool] = None

    show_in_detail_view: typing.Union[None, bool] = None

    show_in_mobile_app: typing.Union[None, bool] = None

    show_in_pod: typing.Union[None, bool] = None

    show_when_task_type_assignment: typing.Union[None, bool] = None

    show_when_task_type_pick_up: typing.Union[None, bool] = None

    show_when_task_type_drop_off: typing.Union[None, bool] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
