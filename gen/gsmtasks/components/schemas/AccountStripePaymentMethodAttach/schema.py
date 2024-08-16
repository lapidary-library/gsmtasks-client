# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class AccountStripePaymentMethodAttach(lapidary.runtime.ModelBase):
    stripe_payment_method_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=255,
        )
    ]

    stripe_customer_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=255,
        )
    ] = None

    set_default: typing.Union[None, bool] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )