# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime


class PasswordResetConfirm(lapidary.runtime.ModelBase):
    uidb64: typing.Annotated[
        str,
        pydantic.Field(
            alias='uidb64',
        )
    ]

    token: typing.Annotated[
        str,
        pydantic.Field(
            alias='token',
        )
    ]

    new_password1: typing.Annotated[
        str,
        pydantic.Field(
            alias='new_password1',
        )
    ]

    new_password2: typing.Annotated[
        str,
        pydantic.Field(
            alias='new_password2',
        )
    ]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
