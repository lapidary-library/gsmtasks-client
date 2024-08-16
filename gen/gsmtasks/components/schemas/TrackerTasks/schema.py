# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.NestedAddress.schema
import gsmtasks.components.schemas.NestedContact.schema
import gsmtasks.components.schemas.TrackerTasks.properties.duration.schema
import uuid


class TrackerTasks(lapidary.runtime.ModelBase):
    contact: gsmtasks.components.schemas.NestedContact.schema.NestedContact

    address: gsmtasks.components.schemas.NestedAddress.schema.NestedAddress

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    state: typing.Union[None, str] = None

    category: typing.Union[None, str] = None

    assignee: typing.Union[None, uuid.UUID] = None

    duration: typing.Union[None, gsmtasks.components.schemas.TrackerTasks.properties.duration.schema.duration] = None

    scheduled_time: typing.Union[None, datetime.datetime] = None

    completed_at: typing.Union[None, datetime.datetime] = None

    cancelled_at: typing.Union[None, datetime.datetime] = None

    failed_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )