# Generated by ariadne-codegen on 2025-02-18 09:26
# Source: queries.graphql
from uuid import UUID

from .async_base_client import AsyncBaseClient
from .base_model import UNSET
from .base_model import UnsetType
from .input_types import EngagementUpdateInput
from .input_types import ManagerTerminateInput
from .manager_engagements import ManagerEngagements
from .manager_engagements import ManagerEngagementsManagers
from .move_engagement import MoveEngagement
from .move_engagement import MoveEngagementEngagementUpdate
from .org_unit_managers import OrgUnitManagers
from .org_unit_managers import OrgUnitManagersOrgUnits
from .terminate_manager import TerminateManager
from .terminate_manager import TerminateManagerManagerTerminate


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):
    async def manager_engagements(
        self, manager_uuid: list[UUID] | None | UnsetType = UNSET
    ) -> ManagerEngagementsManagers:
        query = gql(
            """
            query ManagerEngagements($manager_uuid: [UUID!]) {
              managers(filter: {uuids: $manager_uuid}) {
                objects {
                  current {
                    employee {
                      engagements {
                        uuid
                      }
                    }
                    org_unit_uuid
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"manager_uuid": manager_uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ManagerEngagements.parse_obj(data).managers

    async def org_unit_managers(
        self, uuids: list[UUID] | None | UnsetType = UNSET
    ) -> OrgUnitManagersOrgUnits:
        query = gql(
            """
            query OrgUnitManagers($uuids: [UUID!]) {
              org_units(filter: {uuids: $uuids}) {
                objects {
                  current {
                    name
                    uuid
                    managers {
                      uuid
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"uuids": uuids}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return OrgUnitManagers.parse_obj(data).org_units

    async def terminate_manager(
        self, input: ManagerTerminateInput
    ) -> TerminateManagerManagerTerminate:
        query = gql(
            """
            mutation TerminateManager($input: ManagerTerminateInput!) {
              manager_terminate(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TerminateManager.parse_obj(data).manager_terminate

    async def move_engagement(
        self, input: EngagementUpdateInput
    ) -> MoveEngagementEngagementUpdate:
        query = gql(
            """
            mutation MoveEngagement($input: EngagementUpdateInput!) {
              engagement_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return MoveEngagement.parse_obj(data).engagement_update
