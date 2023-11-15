import os
import json
import time
import meraki
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

#MERAKI API ENVIRONMENT VARIABLES
MERAKI_API_KEY = os.environ['MERAKI_API_KEY']
MERAKI_ORG_ID = os.environ['MERAKI_ORG_ID']

#AZURE API ENVIRONMENT VARIABLES
AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
AZURE_CLIENT_ID = os.environ['AZURE_CLIENT_ID']
AZURE_CLIENT_SECRET = os.environ['AZURE_CLIENT_SECRET']
AZURE_SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
AZURE_RESOURCE_GROUP = os.environ['AZURE_RESOURCE_GROUP']

def find_local_network_gateway(AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, target_ip):
    # Initialize the NetworkManagementClient
    credential = DefaultAzureCredential()
    network_client = NetworkManagementClient(credential, AZURE_SUBSCRIPTION_ID)

    # Get all local network gateways in the specified resource group
    local_gateways = network_client.local_network_gateways.list(AZURE_RESOURCE_GROUP)
    # Check each local gateway for a matching IP address
    for gateway in local_gateways:
        if gateway.gateway_ip_address == target_ip:
            return gateway  # Return the first matching gateway
        
    return None

def check_meraki_wan_uplinks():
    # Connect to the Meraki Dashboard API
    dashboard = meraki.DashboardAPI(MERAKI_API_KEY)

    # Get uplink status from Meraki
    uplink_status = dashboard.appliance.getOrganizationApplianceUplinkStatuses(MERAKI_ORG_ID)
    data = json.loads(json.dumps(uplink_status))

    for i in data:
        uplinks = i['uplinks']

        for wan in uplinks:
            if wan['status'] == 'failed':
                down_ip_address = wan['ip']
                target_appliance = i['networkId']

                # Find the matching Azure Local Network Gateway
                matching_gateway = find_local_network_gateway(AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, down_ip_address)

    # Get uplink status for the target appliance
    target_appliance_uplink_status = dashboard.appliance.getOrganizationApplianceUplinkStatuses(organizationId=MERAKI_ORG_ID, networkIds=target_appliance)
    target_data = json.loads(json.dumps(target_appliance_uplink_status))

    for target_i in target_data:
        target_uplinks = target_i['uplinks']

        for target_wan in target_uplinks:
            if target_wan['status'] == 'active':
                target_ip_address = target_wan['ip']

    # Update the Azure Local Network Gateway with the new IP address
    matching_gateway.local_network_address_space.address_prefixes[0] = target_ip_address

    NetworkManagementClient().local_network_gateways.begin_create_or_update(
        resource_group_name=AZURE_RESOURCE_GROUP,
        local_network_gateway_name=matching_gateway.name,
        local_network_gateway=matching_gateway
        )

# Run the script every 30 seconds
def main():

    while True:
        check_meraki_wan_uplinks()
        time.sleep(30)

if __name__ == "__main__":
    main()