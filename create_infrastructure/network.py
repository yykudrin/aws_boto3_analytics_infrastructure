import boto3
from tags import give_tags


def create_vpc(vpc, cidr='192.168.1.0/24'):
    tags = give_tags('EM_Analytics_VPC')
    response = vpc.create_vpc(
            CidrBlock=cidr,
            InstanceTenancy='default',
            TagSpecifications=[
            { 'ResourceType': 'vpc',
                'Tags': tags
            },
        ]
    )
    return response['Vpc']['VpcId']

def create_subnet(vpc, vpc_id, cidr, az):
    tags = give_tags('EM_Analytics_subnet')
    response = vpc.create_subnet(
                CidrBlock=cidr,
                VpcId=vpc_id,
                AvailabilityZone=az,
                TagSpecifications=[
                    { 'ResourceType': 'subnet',
                    'Tags': tags
                    },
                ]
            )
    return response['Subnet']['SubnetId']


def create_internetgateway(vpc, vpc_id):
    response = vpc.create_internet_gateway()
    ig_id = response['InternetGateway']['InternetGatewayId']
    vpc.attach_internet_gateway(InternetGatewayId=ig_id,
                                         VpcId=vpc_id)
    return ig_id

def create_route_table(vpc, vpc_id):
    tags = give_tags('EM_Analytics_route_table')
    response = vpc.create_route_table(
        DryRun=False,
        VpcId=vpc_id,
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': tags
            }
        ]
    )
    return response['RouteTable']['RouteTableId']

def associate_route_table(vpc, route_table_id, subnet_id):
    response = vpc.associate_route_table(
        DryRun=False,
        RouteTableId=route_table_id,
        SubnetId=subnet_id,
    )

def create_route(vpc, route_table_id, gateway_id, dest_cidr):
    response = vpc.create_route(
        RouteTableId=route_table_id,
        GatewayId=gateway_id,
        DestinationCidrBlock=dest_cidr,
    )
    return response