import boto3
from client_settings import superset_instance_id
from client_settings import region

client = boto3.client('ec2', region_name=region)
response = client.start_instances(
    InstanceIds=[
        superset_instance_id,
    ],
)