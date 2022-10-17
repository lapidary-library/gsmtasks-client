from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid


class TaskMetadata(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    url: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    task: typing.Annotated[str, pydantic.Field()]

    events_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    task_event_notes_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    documents_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    signatures_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    forms_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    forms_completed_count: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=32767.0,
        ),
    ] = lapidary_base.absent.ABSENT

    last_task_event_notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    unassigned_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    assigned_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    accepted_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    transit_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    active_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    completed_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    failed_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    cancelled_duration: typing.Annotated[
        typing.Union[
            typing.Union[
                int,
                str,
            ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    unassigned_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    assigned_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    accepted_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    transit_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    active_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    completed_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    failed_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    cancelled_distance: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            ge=0.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    last_unassigned_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_assigned_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_accepted_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_transit_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_active_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_completed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_failed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    last_cancelled_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


TaskMetadata.update_forward_refs()
