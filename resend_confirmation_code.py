import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

email = ''

response = client.resend_confirmation_code(
    ClientId = '',
    Username = email
)

print(response)