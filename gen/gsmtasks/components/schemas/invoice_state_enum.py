# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum


class InvoiceStateEnum(enum.Enum):
    draft = "draft"
    confirmed = "confirmed"
    overdue = "overdue"
    paid = "paid"
    cancelled = "cancelled"
