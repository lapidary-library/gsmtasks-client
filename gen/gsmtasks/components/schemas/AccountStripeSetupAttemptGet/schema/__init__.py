# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime


class AccountStripeSetupAttemptGet(lapidary.runtime.ModelBase):
    setup_attempt_id: typing.Annotated[
        str,
        pydantic.Field(
            alias='setup_attempt_id',
            max_length=100,
        )
    ]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
