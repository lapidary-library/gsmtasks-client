# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum


class AccountStateEnum(enum.Enum):
    active = "active"
    deactive = "deactive"
    trial_expired = "trial_expired"
    payment_overdue = "payment_overdue"
