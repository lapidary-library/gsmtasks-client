from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent


class UsersListFormat(enum.Enum):
    json = "json"
    xml = "xml"


class UsersList(pydantic.BaseModel):
    q_cursor: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            alias="cursor",
            in_=lapidary_base.ParamPlacement.query,
        ),
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            UsersListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary_base.ParamPlacement.query,
        ),
    ] = lapidary_base.absent.ABSENT

    q_page_size: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            alias="page_size",
            in_=lapidary_base.ParamPlacement.query,
        ),
    ] = lapidary_base.absent.ABSENT

    q_search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            alias="search",
            in_=lapidary_base.ParamPlacement.query,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


UsersList.update_forward_refs()
