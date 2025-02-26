# Generated by ariadne-codegen on 2025-02-05 12:46
# Source: queries.graphql
from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class GetManagerEngagement(BaseModel):
    managers: "GetManagerEngagementManagers"


class GetManagerEngagementManagers(BaseModel):
    objects: list["GetManagerEngagementManagersObjects"]


class GetManagerEngagementManagersObjects(BaseModel):
    current: Optional["GetManagerEngagementManagersObjectsCurrent"]


class GetManagerEngagementManagersObjectsCurrent(BaseModel):
    employee: list["GetManagerEngagementManagersObjectsCurrentEmployee"] | None
    org_unit_uuid: UUID


class GetManagerEngagementManagersObjectsCurrentEmployee(BaseModel):
    engagements: list["GetManagerEngagementManagersObjectsCurrentEmployeeEngagements"]


class GetManagerEngagementManagersObjectsCurrentEmployeeEngagements(BaseModel):
    uuid: UUID


GetManagerEngagement.update_forward_refs()
GetManagerEngagementManagers.update_forward_refs()
GetManagerEngagementManagersObjects.update_forward_refs()
GetManagerEngagementManagersObjectsCurrent.update_forward_refs()
GetManagerEngagementManagersObjectsCurrentEmployee.update_forward_refs()
GetManagerEngagementManagersObjectsCurrentEmployeeEngagements.update_forward_refs()
