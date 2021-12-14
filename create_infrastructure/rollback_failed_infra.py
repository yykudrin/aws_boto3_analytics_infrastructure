# plan:
# delete vpc
# 1. detouch igw from vpc
#    delete igw
# 3. Delete ec2 instances in vpc
# 

import boto3
from settings import region



# Delete network infrastructure
# Delete VPC 192.168.10.0/24 vpc_iaroslav_kudrin vpc-0bacd21e209774cb1

def delete_vpc(vpc_id):
    ec2 = boto3.resource('ec2', region_name=region)
    vpc = ec2.Vpc(vpc_id)
    ec2client = ec2.meta.client
    # 1. Delete ec2 instances in subnet
    for subnet in vpc.subnets.all():
        for instance in subnet.instances.all():
            instance.terminate()


    # 2. Delete Internet gateway
    for gw in vpc.internet_gateways.all():
        vpc.detach_internet_gateway(InternetGatewayId=gw.id)
        gw.delete()

    # 3. Delete Route table associations   
    for rt in vpc.route_tables.all():

        # route table associations
        for rta in rt.associations:
            if not rta.main:
                rta.delete()

    # 4. Delete Route Tables
    for rt in vpc.route_tables.all():
        if not rt.associations:
            rt.delete()
    
    # 5. Delete security group
    for sg in vpc.security_groups.all():
        if sg.group_name != 'default':
            sg.delete()
    
    # 6. Delete nacl
    for nacl in vpc.network_acls.all():
        if not nacl.is_default:
            nacl.delete()
    

    # 7. Delete subnets
    for subnet in vpc.subnets.all():
        for interface in subnet.network_interfaces.all():
            interface.delete()
        subnet.delete()

    # 8. Delete VPC
    ec2client.delete_vpc(VpcId=vpc_id)


delete_vpc('vpc-0e27e0f763a8effa5')
# delete rds

