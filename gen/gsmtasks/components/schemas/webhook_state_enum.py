# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum


class WebhookStateEnum(enum.Enum):
    inactive = "inactive"
    active = "active"
    disabled = "disabled"
