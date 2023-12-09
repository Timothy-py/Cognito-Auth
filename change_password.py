import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

access_token = ''
previous_password = ''
new_password = ''

response = client.change_password(
    PreviousPassword=previous_password,
    ProposedPassword=new_password,
    AccessToken=access_token,
)

print(response)
