from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.location_type_enum


class Location(pydantic.BaseModel):
    type: typing.Annotated[
        gsmtasks.components.schemas.location_type_enum.LocationTypeEnum,
        pydantic.Field(),
    ]

    coordinates: typing.Annotated[
        list[
            float,
        ],
        pydantic.Field(
            max_items=2,
            min_items=2,
        ),
    ]

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


Location.update_forward_refs()
