from flask import Flask, render_template
import api
import json

app=Flask(__name__)


    
@app.route("/")
def table():
    list_repo = api.get_list_repo(user='KentBeck')
    list_urls = api.get_urls(user='KentBeck')
    contributor_list = api.get_contributor(user='KentBeck',urls=list_urls)
    print(contributor_list)
    
    #list_urls = api.get_urls(user='KentBeck')
    #print(api.get_contributor(user='KentBeck'))
    data = zip(list_repo,contributor_list)
    '''
    with open('contributors.json', 'w', encoding='utf8')as file:
        for repository, contributor in data:
            result = [{repository["name"]: contributor}]
            json.dump(result,file)


    
    for repository in list_repo:
        repositories = {}
        repositories["name"] = repository["name"]
        add_repositories(repositories)
    def add_repositories(repositories):
        data["data"].append(repositories)
        print(data)
    '''
    
    
    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
