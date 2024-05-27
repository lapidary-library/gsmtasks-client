# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.NestedAddress.schema
import gsmtasks.components.schemas.PatchedAccount.properties.auto_assign_rotate.schema
import gsmtasks.components.schemas.PatchedAccount.properties.task_duration.schema
import gsmtasks.components.schemas.PatchedAccount.properties.task_expiry_duration_from_complete_after.schema
import gsmtasks.components.schemas.PatchedAccount.properties.task_expiry_duration_from_complete_before.schema
import lapidary.runtime
import uuid


class PatchedAccount(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='name',
            max_length=100,
        )
    ] = None

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    type: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='type',
        )
    ] = None

    slug: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='slug',
            direction=lapidary.runtime.ParamDirection.read,
            regex=r'^[-a-zA-Z0-9_]+$',
        )
    ] = None

    owner: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='owner',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='email',
            max_length=254,
        )
    ] = None

    notification_emails: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='notification_emails',
        )
    ] = None

    review_emails: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='review_emails',
        )
    ] = None

    review_emails_to_assignee: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='review_emails_to_assignee',
        )
    ] = None

    website: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='website',
            max_length=200,
        )
    ] = None

    registry_code: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='registry_code',
            max_length=20,
        )
    ] = None

    vatin: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='vatin',
            max_length=20,
        )
    ] = None

    language: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='language',
        )
    ] = None

    TimezoneEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='TimezoneEnum',
        )
    ] = None

    country_code: typing.Annotated[
        typing.Union[None, str, typing.Any],
        pydantic.Field(
            alias='country_code',
        )
    ] = None

    address: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='address',
        )
    ] = None

    custom_integration_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='custom_integration_url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    RouteDefaultStateEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='RouteDefaultStateEnum',
        )
    ] = None

    DistanceUnitsEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='DistanceUnitsEnum',
        )
    ] = None

    task_duration: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.PatchedAccount.properties.task_duration.schema.task_duration],
        pydantic.Field(
            alias='task_duration',
        )
    ] = None

    task_expiry_duration_from_complete_after: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.PatchedAccount.properties.task_expiry_duration_from_complete_after.schema.task_expiry_duration_from_complete_after],
        pydantic.Field(
            alias='task_expiry_duration_from_complete_after',
        )
    ] = None

    task_expiry_duration_from_complete_before: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.PatchedAccount.properties.task_expiry_duration_from_complete_before.schema.task_expiry_duration_from_complete_before],
        pydantic.Field(
            alias='task_expiry_duration_from_complete_before',
        )
    ] = None

    TaskExpiryStateEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='TaskExpiryStateEnum',
        )
    ] = None

    assignee_proximity_radius: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='assignee_proximity_radius',
            ge=0.0,
            le=2147483647.0,
        )
    ] = None

    DateFormatEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='DateFormatEnum',
        )
    ] = None

    TimeFormatEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='TimeFormatEnum',
        )
    ] = None

    route_start_address: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='route_start_address',
        )
    ] = None

    route_end_address: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='route_end_address',
        )
    ] = None

    optimize_after_create: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='optimize_after_create',
        )
    ] = None

    optimization_objective: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='optimization_objective',
        )
    ] = None

    reference_autogenerate: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='reference_autogenerate',
        )
    ] = None

    reference_offset: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='reference_offset',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    reference_prefix: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='reference_prefix',
            max_length=50,
        )
    ] = None

    reference_length: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='reference_length',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    feature_show_unassigned_to_workers: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_show_unassigned_to_workers',
        )
    ] = None

    feature_task_created_sound: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_task_created_sound',
        )
    ] = None

    feature_change_task_account: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_change_task_account',
        )
    ] = None

    feature_show_tutorial: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_show_tutorial',
        )
    ] = None

    feature_navigation_app_selection: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_navigation_app_selection',
        )
    ] = None

    feature_navigation_use_address: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_navigation_use_address',
        )
    ] = None

    feature_task_accept: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_task_accept',
        )
    ] = None

    feature_task_reject: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_task_reject',
        )
    ] = None

    feature_app_task_search: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_app_task_search',
        )
    ] = None

    FeatureAddressAutosuggestProviderEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='FeatureAddressAutosuggestProviderEnum',
        )
    ] = None

    feature_geocoding_country_code: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='feature_geocoding_country_code',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    feature_document_signing: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_document_signing',
        )
    ] = None

    feature_tracker_reviews_allowed: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_tracker_reviews_allowed',
        )
    ] = None

    feature_tracker_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='feature_tracker_url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    feature_route_folders: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_route_folders',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    feature_route_auto_archive: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_route_auto_archive',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    feature_signature_required: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_signature_required',
        )
    ] = None

    feature_signature_required_task_category: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='feature_signature_required_task_category',
        )
    ] = None

    feature_picture_required: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='feature_picture_required',
        )
    ] = None

    feature_picture_required_task_category: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='feature_picture_required_task_category',
        )
    ] = None

    auto_assign_orders: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='auto_assign_orders',
        )
    ] = None

    auto_assign_max_tasks: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='auto_assign_max_tasks',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    auto_assign_max_distance: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='auto_assign_max_distance',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    auto_assign_time_before: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='auto_assign_time_before',
        )
    ] = None

    auto_assign_rotate: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.PatchedAccount.properties.auto_assign_rotate.schema.auto_assign_rotate],
        pydantic.Field(
            alias='auto_assign_rotate',
        )
    ] = None

    auto_assign_optimize: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='auto_assign_optimize',
        )
    ] = None

    dashboard_task_template: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='dashboard_task_template',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    calendar_task_template: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='calendar_task_template',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    dashboard_worker_limit: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='dashboard_worker_limit',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    stripe_customer_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='stripe_customer_id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    stripe_payment_method_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='stripe_payment_method_id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    billing_method: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_method',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ] = None

    billing_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_name',
            max_length=100,
        )
    ] = None

    billing_company: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_company',
            max_length=100,
        )
    ] = None

    billing_address: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_address',
            max_length=200,
        )
    ] = None

    billing_country: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_country',
            max_length=100,
        )
    ] = None

    billing_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_email',
            max_length=254,
        )
    ] = None

    billing_phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_phone',
            max_length=20,
        )
    ] = None

    billing_vatin: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='billing_vatin',
            max_length=20,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
