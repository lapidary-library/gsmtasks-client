# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import gsmtasks.components.schemas.location
import lapidary.runtime.absent


class NestedAddress(pydantic.BaseModel):
    raw_address: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=250,
        ),
    ] = lapidary.runtime.absent.ABSENT

    formatted_address: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=250,
        ),
    ] = lapidary.runtime.absent.ABSENT

    location: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.location.Location,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    google_place_id: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=250,
        ),
    ] = lapidary.runtime.absent.ABSENT

    point_of_interest: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    street: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        ),
    ] = lapidary.runtime.absent.ABSENT

    house_number: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    apartment_number: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    city: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    state: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    postal_code: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    country: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary.runtime.absent.ABSENT

    country_code: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=2,
        ),
    ] = lapidary.runtime.absent.ABSENT

    geocoded_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    geocode_failed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


NestedAddress.update_forward_refs()
