import requests

# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

baseURI = "https://app.asana.com/api/1.0/"
headers = {'Authorization: Bearer {personal_access_token}'}

print(dir(requests))
print(help(requests.get))


def get_workplace_by_id(workplace_id):
    requests.get(f'{baseURI}/workspaces/{workplace_id}')
