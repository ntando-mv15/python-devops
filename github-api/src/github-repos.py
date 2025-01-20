import requests 

# GitHub API
url = "https://api.github.com/users/ntando-mv15/repos"

def github_api():
    #Fetch data from API
    response = requests.get(url)

    data = response.json() 
    
    # Iterate through the data 
    for repo in data:
        repo_name = repo["name"]
        print(repo_name)
       
github_api()

