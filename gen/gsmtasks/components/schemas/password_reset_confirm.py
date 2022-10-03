from __future__ import annotations

import typing
import lapidary_base
import pydantic


class PasswordResetConfirm(pydantic.BaseModel):
    uidb64: typing.Annotated[str, pydantic.Field()]

    token: typing.Annotated[str, pydantic.Field()]

    new_password1: typing.Annotated[str, pydantic.Field()]

    new_password2: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


PasswordResetConfirm.update_forward_refs()
