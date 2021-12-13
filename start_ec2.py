import boto3
from client_settings import instance_id


client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=[
        instance_id,
    ],
)