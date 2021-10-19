import boto3
from firewall_settings import ingress_permissions_private
from firewall_settings import egress_permissions_private
from firewall_settings import ingress_permissions_public
from firewall_settings import egress_permissions_public
from tags import give_tags

ec2 = boto3.client('ec2')

def create_security_group(vpc_id, group_name, description, ingress_permissions, egress_permissions):
    response = ec2.create_security_group(GroupName=group_name, Description=description, VpcId=vpc_id)
    security_group_id = response['GroupId']
    if egress_permissions:
        egress_rules = ec2.authorize_security_group_egress(
            GroupId=security_group_id,
            IpPermissions=egress_permissions
        )
    if ingress_permissions:
        ingress_rules = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=ingress_permissions
        )
    return response['GroupId']


def create_nacl(vpc_id, nacl_name):
    tags = give_tags(nacl_name)
    response = ec2.create_network_acl(
        DryRun=False,
        VpcId=vpc_id,
        TagSpecifications=[{
            'ResourceType': 'network-acl',
            'Tags': tags
            },
        ]
    )
    return response['NetworkAcl']['NetworkAclId']


def create_nacl_rule(cidr_block, egress, network_acl_id, port_from, port_to, proto, action, number):
    response = ec2.create_network_acl_entry(
        CidrBlock=cidr_block,
        DryRun=False,
        Egress=egress,
        NetworkAclId=network_acl_id,
        PortRange={
            'From': port_from,
            'To': port_to
        },
        Protocol=proto,
        RuleAction=action,
        RuleNumber=number
    )

def assign_nacl_to_subnet(network_acl_id, subnet_id):
    response = ec2.NetworkAcl(
        network_id
    )


if __name__ == "__main__":
    create_security_group('vpc-0d3530b264615016b', 'Analitics_RDS_SG_Iaroslav_Kudrin', 'sg for access to ms sql server from ec2 instances', ingress_permissions_private, egress_permissions_private)
    create_security_group('vpc-0d3530b264615016b', 'Analitics_EC2_SG_Iaroslav_Kudrin', 'sg for access to ec2 from sql instances and from rdp', ingress_permissions_public, egress_permissions_public)
