# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class PatchedPushNotification(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    external_id: typing.Union[None, uuid.UUID] = None

    state: typing.Union[None, str] = None

    notification: typing.Union[None, str] = None

    recipient: typing.Union[None, str] = None

    task: typing.Union[None, str] = None

    event: typing.Union[None, str, typing.Any] = None

    subject: typing.Union[None, str] = None

    message: typing.Union[None, str] = None

    error: typing.Union[None, str] = None

    pending_at: typing.Union[None, datetime.datetime] = None

    failed_at: typing.Union[None, datetime.datetime] = None

    sent_at: typing.Union[None, datetime.datetime] = None

    created_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
