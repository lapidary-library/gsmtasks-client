from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.account
import gsmtasks.components.schemas.app_enum
import gsmtasks.components.schemas.configuration_defaults
import gsmtasks.components.schemas.configuration_notification
import gsmtasks.components.schemas.configuration_settings
import gsmtasks.components.schemas.location
import gsmtasks.components.schemas.readable_user
import lapidary_base.absent


class ConfigurationSerializerV2Auth(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2Features(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2Templates(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2Tracking(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2Permissions(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2LegacyViews(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2Billing(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


class ConfigurationSerializerV2(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    account: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.account.Account,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    user: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.readable_user.ReadableUser,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    is_staff: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    app: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.app_enum.AppEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    version: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    auth: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Auth,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    settings: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.configuration_settings.ConfigurationSettings,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    defaults: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.configuration_defaults.ConfigurationDefaults,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    features: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Features,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    templates: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Templates,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    tracking: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Tracking,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    notifications: typing.Annotated[
        typing.Union[
            list[
                gsmtasks.components.schemas.configuration_notification.ConfigurationNotification,
            ],
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    permissions: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Permissions,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    legacy_views: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2LegacyViews,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    location: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.location.Location,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    is_client_role: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    billing: typing.Annotated[
        typing.Union[
            ConfigurationSerializerV2Billing,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        extra = pydantic.Extra.allow


ConfigurationSerializerV2Auth.update_forward_refs()
ConfigurationSerializerV2Features.update_forward_refs()
ConfigurationSerializerV2Templates.update_forward_refs()
ConfigurationSerializerV2Tracking.update_forward_refs()
ConfigurationSerializerV2Permissions.update_forward_refs()
ConfigurationSerializerV2LegacyViews.update_forward_refs()
ConfigurationSerializerV2Billing.update_forward_refs()
ConfigurationSerializerV2.update_forward_refs()
