# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing_extensions as typing
from lapidary.runtime import *
import gsmtasks.components.schemas.RouteOptimizationSerializerV2.schema


class Response(ResponseEnvelope):
    body: typing.Annotated[list[gsmtasks.components.schemas.RouteOptimizationSerializerV2.schema.RouteOptimizationSerializerV2], ResponseBody()]
