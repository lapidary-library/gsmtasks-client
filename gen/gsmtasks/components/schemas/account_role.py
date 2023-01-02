# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import gsmtasks.components.schemas.account_role_state_enum
import gsmtasks.components.schemas.nested_address
import gsmtasks.components.schemas.vehicle_profile_enum
import lapidary.runtime.absent
import uuid


class AccountRole(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    url: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    account: typing.Annotated[str, pydantic.Field()]

    user: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.account_role_state_enum.AccountRoleStateEnum,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    email: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    display_name: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    phone: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=128,
        ),
    ] = lapidary.runtime.absent.ABSENT

    vehicle_registration_number: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=32,
        ),
    ] = lapidary.runtime.absent.ABSENT

    vehicle_profile: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.vehicle_profile_enum.VehicleProfileEnum,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    vehicle_capacity: typing.Annotated[
        typing.Union[
            list[
                int,
            ],
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    vehicle_speed_factor: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            regex=r"^-?\d{0,1}(?:\.\d{0,1})?$",
        ),
    ] = lapidary.runtime.absent.ABSENT

    vehicle_service_time_factor: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            regex=r"^-?\d{0,1}(?:\.\d{0,1})?$",
        ),
    ] = lapidary.runtime.absent.ABSENT

    route_start_address: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.nested_address.NestedAddress,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    route_end_address: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.nested_address.NestedAddress,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    signature_image: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    is_manager: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    is_worker: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    is_integration: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    is_active: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    is_on_duty: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    show_unassigned: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    last_time_location: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    activated_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    deleted_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    created_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    updated_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


AccountRole.update_forward_refs()
