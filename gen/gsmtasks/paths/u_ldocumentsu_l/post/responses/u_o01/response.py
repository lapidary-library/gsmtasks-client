# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing_extensions as typing
from lapidary.runtime import *
import gsmtasks.components.schemas.Document.schema


class Response(ResponseEnvelope):
    body: typing.Annotated[typing.Union[gsmtasks.components.schemas.Document.schema.Document, list[gsmtasks.components.schemas.Document.schema.Document]], ResponseBody()]