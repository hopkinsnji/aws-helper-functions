def list_org_accounts_old() -> list:
    # import boto3
    '''This returns a list of all the accounts in the org. Better to use the paginator.
        make sure boto3 is imported
    '''

    account_list = []
    org_client = boto3.client("organizations")

    account_response = org_client.list_accounts()
    account_list.extend([account["Id"] for account in account_response["Accounts"]])
    # print(account_response)

    while 'NextToken' in account_response:
            account_response = org_client.list_accounts(NextToken=account_response['NextToken'])
            account_list.extend([account["Id"] for account in account_response["Accounts"]])

            # print(account_response)
    return account_list

def list_org_accounts() -> list:
    # import boto3
    ''' using the paginator
    '''
    org_client = boto3.client("organizations")
    org_paginator = org_client.get_paginator('list_accounts')

    response = org_paginator.paginate()

    account_list = []
    for page in response:
        account_list.extend([account['Id'] for account in page['Accounts']])
        # print(page)
    return account_list

