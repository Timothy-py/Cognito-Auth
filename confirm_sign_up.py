import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

email = ''
confirmation_code = ''

response = client.confirm_sign_up(
    ClientId = '',
    Username = email,
    ConfirmationCode = confirmation_code
)

print(response)