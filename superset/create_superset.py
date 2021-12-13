import boto3
from superset_settings import ec2_ami
from superset_settings import ec2_instance_size
from superset_settings import subnet_id
from superset_settings import sg_id
from superset_settings import AZ


with open('userData.sh', 'r') as f:
    data = f.read()

my_user_data = data

ec2 = boto3.client('ec2')
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
            'NetworkCardIndex': 0
            'Groups': [
                sg_id,
            ],
            'SubnetId': subnet_id,
        },
    ],
)

print('superset_id=', response['Instances'][0]['InstanceId'])