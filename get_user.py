import boto3

client = boto3.client('cognito-idp', region_name='eu-west-1')

access_token = ''

response = client.get_user(
    AccessToken=access_token
)

email, sub, username = None, None, None

for attr in response['UserAttributes']:
    if attr['Name'] == 'sub':
        sub = attr['Value']
    elif attr['Name'] == 'name':
        username = attr['Value']
    elif attr['Name'] == 'email':
        email = attr['Value']

print('username', username)
print('email', email)
print('sub', sub)