#configuration to manage api calls
config = Config(
        connect_timeout=1, read_timeout=1,
        retries={'max_attempts': 20, 'mode': 'adaptive'}, )
# https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html