import boto3



def _aws_role_to_client(role_arn, session_name, client, token_life=900):
    """ 
    This takes in a role and returns a boto3 client. Previeouly, I used functions which returned credentials,
    but those credentials are always used to create clients, so I pass the aws service to the function
    and have it return the client.
    """
    sts_client = boto3.client("sts")
    try:
        assumed_role_object = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name,
            DurationSeconds=int(token_life),
        )
        credentials = assumed_role_object["Credentials"]

        return boto3.client(
                client,
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
            )

    except ClientError as e:
        print(e)
        return False

    
    def _aws_role_to_client_with_region(role_arn, session_name, client, token_life=900, region):
    """ 
    This takes in a role and returns a boto3 client. Same as above but this puts you in a region you specify. 
    I won't need to use it this way if I am working in on region only.
    """
    sts_client = boto3.client("sts")
    try:
        assumed_role_object = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name,
            DurationSeconds=int(token_life),
        )
        credentials = assumed_role_object["Credentials"]

        return boto3.client(
                client,
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
                region = region
            )

    except ClientError as e:
        print(e)
        return False


'''
Alternatively, when working with many accounts and regions, I could just pass the account and region and hardcode the 
role inside function. Use f strings to put the account number into the arn.
'''