# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class TaskMetadata(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID]

    url: typing.Union[None, str]

    task: str

    events_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    task_event_notes_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    documents_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    signatures_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    forms_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    forms_completed_count: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        )
    ] = None

    last_task_event_notes: typing.Union[None, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    NullableTaskDuration: typing.Union[None, int, str] = None

    unassigned_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    assigned_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    accepted_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    transit_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    active_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    completed_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    failed_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    cancelled_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    last_unassigned_at: typing.Union[None, datetime.datetime] = None

    last_assigned_at: typing.Union[None, datetime.datetime] = None

    last_accepted_at: typing.Union[None, datetime.datetime] = None

    last_transit_at: typing.Union[None, datetime.datetime] = None

    last_active_at: typing.Union[None, datetime.datetime] = None

    last_completed_at: typing.Union[None, datetime.datetime] = None

    last_failed_at: typing.Union[None, datetime.datetime] = None

    last_cancelled_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
