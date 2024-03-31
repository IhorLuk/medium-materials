from minio import Minio

# create client with creadentials for created user
client = Minio(
    "localhost:9000",
    access_key="dev_user_01",
    secret_key="devpassword01",
    secure=False
)

bucket_name = "test-bucket"

# check if bucket already exists
found = client.bucket_exists(bucket_name)

# create new bucket
if not found:
    client.make_bucket(bucket_name)

# upload local file to MiniO
destination_file = 'test.csv'
source_file = 'test.csv'
client.fput_object(bucket_name, destination_file, source_file,)