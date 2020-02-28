import asana
# import pycurl
import urllib
from


# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# CONSTRUCT ASANA CLIENT
client = asana.Client.access_token(personal_access_token)


# Set things up to send the name of this script to us to show that you succeeded! This is optional.
# client.options['client_name'] = "hello_world_python"


project = client.projects
print(dir(project))
print(project)

# Get your user info
me = client.users.me()
print(me)
print("The username  is: " + me["name"])
