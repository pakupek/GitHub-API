import requests
import json
from urllib.request import urlopen
ACCESS_KEY = "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"


def get_list_repo(user):
    endpoint = f'https://api.github.com/users/{user}/repos'
    headers = {
        "Authorization": f'token {ACCESS_KEY}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_contributors(user,repo):
    endpoint = f'https://api.github.com/repos/{user}/{repo}/contributors?per_page=100'
    headers = {
        "Authorization": f'token {ACCESS_KEY}'
    }
    r = requests.get(endpoint, headers)
    r.raise_for_status()
    return len(r.json())
    

def get_urls(user):
    list_repo = get_list_repo(user)
    list_url = []
    for repository in list_repo:
        endpoint ="https://api.github.com/repos/{}/{}/contributors?per_page=100".format(user,repository["name"])
        url = endpoint
        list_url.append(url)
    return list_url


def get_contributor(user,urls):
    list_repo = get_list_repo(user)
    urls = get_urls(user)
    list_contributors = []
    header ={
        "Authorization": f'token {ACCESS_KEY}'
        }
    for url in urls:   
        r = requests.get(url,header)
        try:
            length = len(r.json())
            list_contributors.append(length)
        except json.decoder.JSONDecodeError:
            empty = 0
            list_contributors.append(empty)
    return list_contributors
    

def get_default_branch(user):
    list_repo = get_list_repo(user)
    branch_list = []
    header ={
        "Authorization": f'token {ACCESS_KEY}'
        }
    for repository in list_repo:
        endpoint ="https://api.github.com/repos/{}/{}/branches".format(user,repository['name'])
        response = requests.get(endpoint,header)
        json_response = response.json()
        print(json_response[""]["name"])
       
        
       
        
       
        
        
    return branch_list