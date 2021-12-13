import boto3
from client_settings import superset_instance_id


client = boto3.client('ec2')
response = client.stop_instances(
    InstanceIds=[
        superset_instance_id,
        ],
)