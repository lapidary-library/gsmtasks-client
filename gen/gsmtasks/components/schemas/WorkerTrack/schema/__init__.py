# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.WorkerTrack.properties.properties.schema
import lapidary.runtime


class WorkerTrack(lapidary.runtime.ModelBase):
    GisFeatureEnum: typing.Union[None, str] = None

    id: typing.Union[None, str] = None

    geometry: typing.Union[None, typing.Any] = None

    properties: typing.Union[None, gsmtasks.components.schemas.WorkerTrack.properties.properties.schema.properties] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
