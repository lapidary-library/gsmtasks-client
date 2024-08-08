# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic


class PasswordResetConfirm(pydantic.BaseModel):
    uidb64: typing.Annotated[str, pydantic.Field()]

    token: typing.Annotated[str, pydantic.Field()]

    new_password1: typing.Annotated[str, pydantic.Field()]

    new_password2: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


PasswordResetConfirm.update_forward_refs()