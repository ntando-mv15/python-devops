import requests 

# GitHub API
url = "https://api.github.com/users/ntando-mv15/repos"

def github_api():
    #Fetch data from API
    response = requests.get(url)

    data = response.json() 
    
    # Iterate through the data 
    for repo in data:
        if status_code == 200:
            repo_name = repo["name"]
            file_path = "/mnt/c/Users/NTAND/python-scripting/github-api/repos/repos.txt"
            with open(file_path, "a") as new_file:    
                new_file.write(repo_name + "\n")
       
github_api()

