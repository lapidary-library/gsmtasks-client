# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime


class TaskAccountChange(lapidary.runtime.ModelBase):
    account: str

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
