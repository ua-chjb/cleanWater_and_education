from components.read_secrets import get_parameter


REGION = "us-west-1"

aws_region = get_parameter(REGION, "/we_better/aws_region")
aws_bucket_name = get_parameter(REGION, "/we_better/aws_bucket_name")
