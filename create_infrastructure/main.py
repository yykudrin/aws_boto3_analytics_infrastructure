from network import create_vpc
from network import create_subnet
from network import create_internetgateway
from firewalls import create_security_group
from firewall_settings import ingress_permissions_private
from firewall_settings import egress_permissions_private
from firewall_settings import ingress_permissions_public
from firewall_settings import egress_permissions_public
from firewalls import create_nacl
from firewalls import create_nacl_rule
from firewalls import assign_nacl_to_subnet
from database import create_rds
from database import create_db_subnet_group
from network import create_route_table
from network import associate_route_table
from network import create_route


# Create Network
vpc = create_vpc()
subnet_id_public = create_subnet(vpc, '192.168.1.0/25', 'us-west-1a')
subnet_id_private_1 = create_subnet(vpc, '192.168.1.128/26', 'us-west-1a')
subnet_id_private_2 = create_subnet(vpc, '192.168.1.192/26', 'us-west-1b')
gateway_id = create_internetgateway(vpc)

# Create Security Groups
sg_private = create_security_group(vpc, 'Analitics_RDS_SG_Iaroslav_Kudrin', 'sg for access to ms sql server from ec2 instances', ingress_permissions_private, egress_permissions_private)
sg_public = create_security_group(vpc, 'Analitics_EC2_SG_Iaroslav_Kudrin', 'sg for access to ec2 from sql instances and from rdp', ingress_permissions_public, egress_permissions_public)

# Create Route Tables - Not Ready yet
route_table_id = create_route_table(vpc)
associate_route_table(route_table_id, subnet_id_public)
associate_route_table(route_table_id, subnet_id_private_1)
associate_route_table(route_table_id, subnet_id_private_2)
create_route(route_table_id, gateway_id, '0.0.0.0/0')


# Create NACL


# Assossiate NACLs with subnets


# Create NACL Rules
# create_nacl_rule('192.168.1.0/25', False, nacl_id_private, 1433, 1433, '6', 'allow', 100)
# create_nacl_rule('192.168.1.0/25', True, nacl_id_private, 1024, 65535, '6', 'allow', 100)

# create_nacl_rule('0.0.0.0/0', False, nacl_id_public, 1, 65535, '-1', 'allow', 100)
# create_nacl_rule('0.0.0.0/0', True, nacl_id_public, 1, 65535, '-1', 'allow', 100)

# Create RDS
create_db_subnet_group(subnet_id_private_1, subnet_id_private_2)
create_rds(sg_private)


