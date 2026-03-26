import boto3


def get_parameter(region, name):
    client = boto3.client("ssm", region_name=region)
    return client.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]
