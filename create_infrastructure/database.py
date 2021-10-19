import boto3
from tags import give_tags

rds = boto3.client('rds')


def create_rds(SG, inst_class='db.t3.micro', engine='postgres'):
    tags = give_tags('Analytics_DB')

    response = rds.create_db_instance(
    DBName='Analytics_db',
    DBInstanceIdentifier='analyticsdbid',
    AllocatedStorage=30,
    MaxAllocatedStorage=100,
    DBInstanceClass=inst_class,
    Engine=engine,
    MasterUsername='Administrator',
    MasterUserPassword='User1234',
    VpcSecurityGroupIds=[
        SG,
    ],
    BackupRetentionPeriod=0,
    Port=5432,
    MultiAZ=False,
    EngineVersion='13.4',
    AutoMinorVersionUpgrade=True,
    PubliclyAccessible=False,
    Tags=tags,
    StorageType='gp2',
    StorageEncrypted=False,
    CopyTagsToSnapshot=False,
    DeletionProtection=False,
    DBSubnetGroupName='Analytics_DB_subnet_group_explisit',
)


def create_db_subnet_group(subnet_id_1, subnet_id_2):
    tags = give_tags('Analytics_DB_subnet_group')

    response = rds.create_db_subnet_group(
        DBSubnetGroupName='Analytics_DB_subnet_group_explisit',
        DBSubnetGroupDescription='db_subnet_group',
        SubnetIds=[
            subnet_id_1,
            subnet_id_2,
        ],
        Tags=tags
    )
    return 'Analytics_DB_subnet_group_explisit'