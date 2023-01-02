# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum
import lapidary.runtime.absent


class FormrulesListFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class FormrulesList(pydantic.BaseModel):
    q_account: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="account",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_cursor: typing.Annotated[
        typing.Union[
            int,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="cursor",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            FormrulesListFormat,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_page_size: typing.Annotated[
        typing.Union[
            int,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="page_size",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    q_search: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="search",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


FormrulesList.update_forward_refs()
