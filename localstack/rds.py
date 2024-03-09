import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"
rds = boto3.client("rds", endpoint_url=endpoint_url)

# create cluster, only in pro localstack package
create_cluster_resp = rds.create_db_cluster(
    DBClusterIdentifier="db1",
    Engine="aurora-postgresql",
    DatabaseName="test-aurora",
    MasterUsername="myuser",
    MasterUserPassword="mypassword"
)

print(create_cluster_resp)