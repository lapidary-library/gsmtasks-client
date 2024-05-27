# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class Metafield(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        str,
        pydantic.Field(
            alias='account',
        )
    ]

    key: typing.Annotated[
        str,
        pydantic.Field(
            alias='key',
            max_length=20,
            regex=r'^[a-z0-9_]+$',
        )
    ]

    field_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='field_name',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='created_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    updated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='updated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    ordering: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='ordering',
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    namespace: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='namespace',
            max_length=20,
            regex=r'^[a-z0-9_]+$',
        )
    ] = None

    ValueTypeEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='ValueTypeEnum',
        )
    ] = None

    label: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='label',
            max_length=40,
        )
    ] = None

    choices: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='choices',
        )
    ] = None

    choices_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='choices_url',
            max_length=2048,
        )
    ] = None

    is_editable: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_editable',
        )
    ] = None

    is_editable_assignee: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_editable_assignee',
        )
    ] = None

    is_required: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_required',
        )
    ] = None

    is_persistent: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_persistent',
        )
    ] = None

    is_cloned: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_cloned',
        )
    ] = None

    is_searchable: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='is_searchable',
        )
    ] = None

    show_in_list_view: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_in_list_view',
        )
    ] = None

    show_in_detail_view: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_in_detail_view',
        )
    ] = None

    show_in_mobile_app: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_in_mobile_app',
        )
    ] = None

    show_in_pod: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_in_pod',
        )
    ] = None

    show_when_task_type_assignment: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_when_task_type_assignment',
        )
    ] = None

    show_when_task_type_pick_up: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_when_task_type_pick_up',
        )
    ] = None

    show_when_task_type_drop_off: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_when_task_type_drop_off',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )