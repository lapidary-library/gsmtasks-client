# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing_extensions as typing
from lapidary.runtime import *
import gsmtasks.components.schemas.GSMTasksError.schema


class Response(ResponseEnvelope):
    body: typing.Annotated[gsmtasks.components.schemas.GSMTasksError.schema.GSMTasksError, ResponseBody()]
