import boto3
from client_settings import instance_id


response = client.stop_instances(
    InstanceIds=[
        instance_id,
        ],
)
