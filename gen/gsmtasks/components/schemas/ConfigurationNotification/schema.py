# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class ConfigurationNotification(lapidary.runtime.ModelBase):
    level: str

    message: str

    url: typing.Union[None, str]

    persist: typing.Union[None, bool] = None

    open_in_new_window: typing.Union[None, bool] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )