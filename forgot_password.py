import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

email = ''

response = client.forgot_password(
    ClientId='',
    Username=email
)

print(response)