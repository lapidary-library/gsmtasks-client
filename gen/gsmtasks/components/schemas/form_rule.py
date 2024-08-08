# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import lapidary.runtime.absent
import uuid


class FormRuleRules(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


class FormRule(pydantic.BaseModel):
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

    is_active: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        ),
    ]

    edit_url: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        ),
    ]

    view_url: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        ),
    ] = lapidary.runtime.absent.ABSENT

    pdf_url: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        ),
    ] = lapidary.runtime.absent.ABSENT

    rules: typing.Annotated[FormRuleRules, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


FormRuleRules.update_forward_refs()
FormRule.update_forward_refs()