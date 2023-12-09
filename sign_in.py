import boto3


client = boto3.client('cognito-idp', region_name='eu-west-1')

email = ''
password = ''

response = client.initiate_auth(
    ClientId='',
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': email,
        'PASSWORD': password
    }
)

print(f"Access Token: {response['AuthenticationResult']['AccessToken']}")
print(f"Refresh Token: {response['AuthenticationResult']['RefreshToken']}")
