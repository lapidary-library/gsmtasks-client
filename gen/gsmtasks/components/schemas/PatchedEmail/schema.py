# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class PatchedEmail(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=34,
        )
    ] = None

    state: typing.Union[None, str] = None

    notification: typing.Union[None, str] = None

    sender: typing.Union[None, str] = None

    from_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=254,
        )
    ] = None

    reply_to_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=254,
        )
    ] = None

    to_emails: typing.Union[None, list[str]] = None

    subject: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=250,
        )
    ] = None

    message: typing.Union[None, str] = None

    sent_at: typing.Union[None, datetime.datetime] = None

    failed_at: typing.Union[None, datetime.datetime] = None

    received_at: typing.Union[None, datetime.datetime] = None

    created_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
