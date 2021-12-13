import boto3
from client_settings import superset_instance_id


response = client.stop_instances(
    InstanceIds=[
        superset_instance_id,
        ],
)