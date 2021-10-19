import boto3
from client_settings import instance_id


response = client.start_instances(
    InstanceIds=[
        instance_id,
    ],
)