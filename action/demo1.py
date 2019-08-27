from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, SUBSCRIPTION_ID, GROUP_NAME, LOCATION, VM_NAME, client_id, secret, tenant):
        SUBSCRIPTION_ID = '2f50f202-0a84-4c8c-a929-fcc5a3174590'
        GROUP_NAME = 'vm2'
        LOCATION ='West India'
        VM_NAME = 'vm2del'
        
        def get_credentials():
            credentials = ServicePrincipalCredentials(
                client_id = '7aae3fd9-9324-463f-89f5-7c4144971bfb',
                secret = 'MJOJszdQ2fl]xYQQ5Lm+]hAM2vgR0e+5',
                tenant = 'd5656af4-b7b3-45b9-9346-fb0547921fb7'
            )
        
            return credentials
        
        def delete_resources(resource_group_client):
            resource_group_client.resource_groups.delete(GROUP_NAME)

        credentials = get_credentials()
        resource_group_client = ResourceManagementClient(
            credentials,
            SUBSCRIPTION_ID
        )
        network_client = NetworkManagementClient(
            credentials,
            SUBSCRIPTION_ID
        )
        compute_client = ComputeManagementClient(
            credentials,
            SUBSCRIPTION_ID
        )

        delete_resources(resource_group_client)
