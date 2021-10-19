import boto3
from tags import give_tags


vpc = boto3.client('ec2')

def create_vpc(cidr='192.168.1.0/24'):
    tags = give_tags('Analytics_VPC_Iaroslav_Kudrin')
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

def create_subnet(vpc_id, cidr, az):
    response = vpc.create_subnet(
                CidrBlock=cidr,
                VpcId=vpc_id,
                AvailabilityZone=az,
            )
    return response['Subnet']['SubnetId']


def create_internetgateway(vpc_id):
    response = vpc.create_internet_gateway()
    ig_id = response['InternetGateway']['InternetGatewayId']
    vpc.attach_internet_gateway(InternetGatewayId=ig_id,
                                         VpcId=vpc_id)
    return ig_id

def create_route_table(vpc_id):
    tags = give_tags('analytics_route_table')
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

def associate_route_table(route_table_id, subnet_id):
    response = vpc.associate_route_table(
        DryRun=False,
        RouteTableId=route_table_id,
        SubnetId=subnet_id,
    )

def create_route(route_table_id, gateway_id, dest_cidr):
    response = vpc.create_route(
        RouteTableId=route_table_id,
        GatewayId=gateway_id,
        DestinationCidrBlock=dest_cidr,
    )
    return response