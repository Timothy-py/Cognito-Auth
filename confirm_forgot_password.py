import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

email = ''
confirmation_code = ''
password = ''

response = client.confirm_forgot_password(
    ClientId='',
    Username=email,
    ConfirmationCode=confirmation_code,
    Password=password
)

print(response)
