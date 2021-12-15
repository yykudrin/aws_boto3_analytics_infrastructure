import boto3
from client_settings import ami
from client_settings import ec2_instance_size
from client_settings import subnet_id
from client_settings import sg_id
from client_settings import AZ
from client_settings import region


my_user_data = ''

ec2 = boto3.client('ec2', region_name=region)
response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 30,
                'VolumeType': 'standard',
                'Encrypted': False
            },
        },
    ],
    ImageId=ami,
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
            'Groups': [
                sg_id,
            ],
            'SubnetId': subnet_id,
            'InterfaceType': 'interface',
            'NetworkCardIndex': 0
        },
    ],
)

print(response['Instances'][0]['InstanceId'])