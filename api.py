import requests
import json, urllib.request
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

'''
def get_contributor(user):
    list_repo = get_list_repo(user)
    list_url =[]
    list_contributors =[]
    for repository, url in zip(list_repo,list_url):
        base = "https://api.github.com/repos/{}".format(user)
        extend = '/{}/contributors?per_page=100'.format(repository["name"])
        url = base+extend
        list_url.append(url)
        header ={
                "Authorization": f'token {ACCESS_KEY}'
        }
        response = requests.get(url, header)
        response.raise_for_status()
        result = len(response.json())
        list_contributors.append(result)
        
        return list_contributors
    print(list_url)
    
    
    for url in list_url:
        endpoint = url   
        header ={
        "Authorization": f'token {ACCESS_KEY}'
        }
        response = requests.get(endpoint, header)
        response.raise_for_status()
        result = len(response.json())
        list_contributors.append(result)
        return len(response.json())
    return list_contributors
    '''

def get_contributor(user,urls):
    list_repo = get_list_repo(user)
    urls = get_urls(user)
    list_contributors = []
    for url in urls:   
        header ={
        "Authorization": f'token {ACCESS_KEY}'
        }
        r = requests.get(url, header)
        result = len(r.json())
        if len(r.json()) is None:
            list_contributors.append(result)
        print(result)
        list_contributors.append(result)
    
    return list_contributors
    



'''
def contributors(user):
    list_url = get_urls(user)
    list_contributors =[]
    for url in list_url:
        contributor = get_contributor(user='KentBeck')
        list_contributors.append(contributor)
    return list_contributors
'''