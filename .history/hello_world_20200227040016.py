import asana
# import pycurl
import urllib3
from urllib3 import request


# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# CONSTRUCT ASANA CLIENT
asana_api = asana.Client.access_token(personal_access_token)

# url = "https://app.asana.com/api/1.0/projects"

# see your workspaces
# Result: [{u'id': 123456789, u'name': u'asanapy'}]
print(dir(asana_api.workspaces.find_all()))
myspaces = asana_api.workspaces.find_all()
print(myspaces)

# create a new project
# asana_api.create_project('test project', myspaces[0]['id'])

# create a new task
# asana_api.create_task(
#     'yetanotherapitest', myspaces[0]['id'], assignee_status='later', notes='some notes')


# Get your user info
me = asana_api.users.me()
print(me)
print("Hello,  " + me["name"])
