from components.read_secrets import get_parameter


REGION = "us-west-1"

aws_access_key = get_parameter(REGION, "/we_better/aws_access_key_id")
aws_secret_key = get_parameter(REGION, "/we_better/aws_secret_access_key")
aws_region = get_parameter(REGION, "/we_better/aws_region")
aws_bucket_name = get_parameter(REGION, "/we_better/aws_bucket_name")
