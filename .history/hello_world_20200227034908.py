import asana
# import pycurl
import urllib
from urllib import Request


# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# CONSTRUCT ASANA CLIENT
client = asana.Client.access_token(personal_access_token)

url = "https://app.asana.com/api/1.0/projects"
request = Request(url)
request.add_header('personal_access_token', personal_access_token)
response = urlopen(Request)
print(response.read())


# Set things up to send the name of this script to us to show that you succeeded! This is optional.
# client.options['client_name'] = "hello_world_python"


# project = client.projects
# print(dir(project))
# print(project)

# Get your user info
me = client.users.me()
print(me)
print("Hello,  " + me["name"])
