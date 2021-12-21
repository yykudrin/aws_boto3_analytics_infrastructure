import boto3
import os
import sys

from superset_settings import ec2_ami
from superset_settings import ec2_instance_size
from superset_settings import subnet_id
from superset_settings import sg_id
from superset_settings import AZ
from superset_settings import region


with open(os.path.join(sys.path[0], "userData.sh"), 'r') as f:
    data = f.read()

my_user_data = data

ec2 = boto3.client('ec2', region_name=region)
response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'standard',
                'Encrypted': False
            },
        },
    ],
    ImageId=ec2_ami,
    InstanceType=ec2_instance_size,
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    Placement={
        'AvailabilityZone': AZ,
        'Tenancy': 'default',
    },
    UserData= my_user_data,
    DisableApiTermination=False,
    DryRun=False,
    EbsOptimized=False,

    InstanceInitiatedShutdownBehavior='stop',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            'DeviceIndex': 0,
            'InterfaceType': 'interface',
            'NetworkCardIndex': 0,
            'Groups': [
                sg_id,
            ],
            'SubnetId': subnet_id,
        },
    ],
)

# add rule to security group open tcp port 8088 allow incoming traffic
data = ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {'IpProtocol': 'tcp',
        'FromPort': 8088,
        'ToPort': 8088,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)

instance_id = response['Instances'][0]['InstanceId']
print('superset_id=', instance_id)

# wait for 5 second to get public ip
time.sleep(2)


instance = ec2.describe_instances(
    InstanceIds=[instance_id]
)

public_ip_addr = instance['Reservations'][0]['Instances'][0]['PublicIpAddress']


print('Connection URL is\n', f'HTTP://{public_ip_addr}:8088/')