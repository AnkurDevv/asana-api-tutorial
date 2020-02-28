import requests

# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

baseURI = "https://app.asana.com/api/1.0"
headers = {'Authorization': f'Bearer {personal_access_token}'}


def get_workplace_by_id(workplace_id):
    print(f'{baseURI}/workspaces/{workplace_id}')
    r = requests.get(f'{baseURI}/workspaces/{workplace_id}', headers=headers)
    print(r.text)
    return r


def get_projects(workplace_id):
    r = requests.get(
        f'{baseURI}/projects?workspace={workplace_id}', headers=headers)
    return r.text


def get_a_project(project_id):
    r = requests.get(
        f'{baseURI}/projects/{project_id}', headers=headers)
    return r.text


def get_task(project_id):
    r = requests.get(
        f'{baseURI}/tasks?project={project_id}', headers=headers)
    return r.text


# print(get_workplace_by_id('542210956033110'))

# print(get_projects('542210956033110'))
# print(get_a_project('1163857214612401'))
print(get_task('546282206576889'))
