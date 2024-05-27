# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.NestedAddress.schema
import gsmtasks.components.schemas.NestedContact.schema
import gsmtasks.components.schemas.TaskEventTask.properties.actions.schema
import gsmtasks.components.schemas.TaskEventTask.properties.counts.schema
import gsmtasks.components.schemas.TaskEventTask.properties.duration.schema
import gsmtasks.components.schemas.TaskEventTask.properties.forms.schema
import gsmtasks.components.schemas.TaskEventTask.properties.metafields.schema
import lapidary.runtime
import uuid


class TaskEventTask(lapidary.runtime.ModelBase):
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

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    orderer_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='orderer_name',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    contact_address_external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='contact_address_external_id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    calendar_time: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='calendar_time',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    completed_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='completed_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    cancelled_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='cancelled_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    assignee_proximity: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='assignee_proximity',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    forms: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskEventTask.properties.forms.schema.forms],
        pydantic.Field(
            alias='forms',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    trackers: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='trackers',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    recurrence: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='recurrence',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    issues: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='issues',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    counts: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskEventTask.properties.counts.schema.counts],
        pydantic.Field(
            alias='counts',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    actions: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskEventTask.properties.actions.schema.actions],
        pydantic.Field(
            alias='actions',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    created_by: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='created_by',
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

    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
        )
    ] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=100,
        )
    ] = None

    reference: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='reference',
            max_length=100,
        )
    ] = None

    barcodes: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='barcodes',
        )
    ] = None

    assignee: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='assignee',
        )
    ] = None

    order: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='order',
        )
    ] = None

    orderer: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='orderer',
            direction=lapidary.runtime.ParamDirection.write,
        )
    ] = None

    route: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='route',
        )
    ] = None

    TaskCategoryEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='TaskCategoryEnum',
        )
    ] = None

    NestedContact: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedContact.schema.NestedContact],
        pydantic.Field(
            alias='NestedContact',
        )
    ] = None

    NestedAddress: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='NestedAddress',
        )
    ] = None

    contact_address: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='contact_address',
        )
    ] = None

    description: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='description',
        )
    ] = None

    complete_after: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='complete_after',
        )
    ] = None

    complete_before: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='complete_before',
        )
    ] = None

    scheduled_time: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='scheduled_time',
        )
    ] = None

    auto_assign: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='auto_assign',
        )
    ] = None

    position: typing.Annotated[
        typing.Union[None, float],
        pydantic.Field(
            alias='position',
            ge=0.0,
            le=253402300799.0,
        )
    ] = None

    priority: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='priority',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    duration: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskEventTask.properties.duration.schema.duration],
        pydantic.Field(
            alias='duration',
        )
    ] = None

    size: typing.Annotated[
        typing.Union[None, list[int]],
        pydantic.Field(
            alias='size',
        )
    ] = None

    documents: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='documents',
        )
    ] = None

    signatures: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='signatures',
        )
    ] = None

    metafields: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskEventTask.properties.metafields.schema.metafields],
        pydantic.Field(
            alias='metafields',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
