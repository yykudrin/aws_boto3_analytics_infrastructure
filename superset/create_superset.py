import boto3



my_user_data = ''

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
    ImageId='ami-036d46416a34a611c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    Placement={
        'AvailabilityZone': 'us-west-2a',
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
        },
    ],
)

print(response['Instances'][0]['InstanceId'])