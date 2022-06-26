from flask import Flask, render_template
import api
import json

app=Flask(__name__)


    
@app.route("/")
def table():
    list_repo = api.get_list_repo(user='KentBeck')
    #print(list_repo)
    list_urls = api.get_urls(user='KentBeck')
    contributor_list = api.get_contributor(user='KentBeck',urls=list_urls)
    branch_list = api.get_default_branch(user='KentBeck')
    
    
    data = zip(list_repo,contributor_list,branch_list)
   
    
    
    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
