# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum


class EmailStateEnum(enum.Enum):
    queued = "queued"
    over_quota = "over_quota"
    sent = "sent"
    failed = "failed"
    received = "received"
