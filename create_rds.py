#creating rds instance in aws using boto3
import boto3

rds=boto3.client('rds',region_name='ap-south-1')
response=rds.create_db_instance(
    DBInstanceIdentifier='FinanceWithPython',
    AllocatedStorage= 20,
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='admin', #Specify an alphanumeric string that defines the login ID for the master user.
    MasterUserPassword='admincreate', #At least 8 printable ASCII characters. Can't contain any of the following: / (slash), '(single quote), "(double quote) and @ (at sign).
    VpcSecurityGroupIds=['sg-0896fa0bb33a88949'],
    MultiAZ=False
)
print(response)