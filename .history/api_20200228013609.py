# import requests in order to make api calls to asana
import requests

# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# Notice that we removed one slash from front of it
baseURI = "https://app.asana.com/api/1.0"
headers = {'Authorization': f'Bearer {personal_access_token}'}


# API TO GET WORKPLACE BY ID
def get_workplace_by_id(workplace_id):
    print(f'{baseURI}/workspaces/{workplace_id}')
    r = requests.get(f'{baseURI}/workspaces/{workplace_id}', headers=headers)
    print(r.text)
    return r

# API TO GET PROJECTS RELATED TO A WORKSPACE


def get_projects(workplace_id):
    r = requests.get(
        f'{baseURI}/projects?workspace={workplace_id}', headers=headers)
    return r.text

# API TO GET A PROJECT USING ID


def get_a_project(project_id):
    r = requests.get(
        f'{baseURI}/projects/{project_id}', headers=headers)
    return r.text

# API TO GET A PARTICULAR TASK


def get_task(project_id):
    r = requests.get(
        f'{baseURI}/tasks?project={project_id}', headers=headers)
    return r.text

# API TO UPDATE A TASK NAME


def update_a_task(task_id, task_content):
    r = requests.put(
        f'{baseURI}/tasks/{task_id}', headers=headers, data=task_content)
    return r

# WRITE AN API THAT GETS A TASK AND THEN ADDS A SUBTASK


def create_subtask():
    pass

    # print(get_workplace_by_id('542210956033110'))

    # print(get_projects('542210956033110'))
    # print(get_a_project('1163857214612401'))
data = {
    "name": 'mission kobo changed'
}

print(get_task('1163857214612401'))
# print(update_a_task('1163857214612404', data))
