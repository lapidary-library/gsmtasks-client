# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime
import uuid


class AccountRoleToken(lapidary.runtime.ModelBase):
    token: typing.Union[None, uuid.UUID]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
