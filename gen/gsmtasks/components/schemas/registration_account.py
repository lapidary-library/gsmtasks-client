from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.blank_enum
import gsmtasks.components.schemas.country_code_enum
import gsmtasks.components.schemas.language_enum
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.timezone_enum
import gsmtasks.components.schemas.type21d_enum
import lapidary_base.absent
import uuid


class RegistrationAccount(pydantic.BaseModel):
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

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    type: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.type21d_enum.Type21dEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    language: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.language_enum.LanguageEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    timezone: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.timezone_enum.TimezoneEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    country_code: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.country_code_enum.CountryCodeEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    website: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


RegistrationAccount.update_forward_refs()
