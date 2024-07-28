# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import uuid


class AccountRoleToken(lapidary.runtime.ModelBase):
    token: typing.Union[None, uuid.UUID] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
