import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

username = ''
password = ''
email = ''

try:
    response = client.sign_up(
        ClientId='',
        Username=email,
        Password=password,
        UserAttributes=[
            {
                'Name': 'name',
                'Value': username,
            },
        ],
    )
except Exception as e:
    print(f"Exception {e}")
    # print("User already exists")
else:
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f"User created successfully {response['UserSub']}")