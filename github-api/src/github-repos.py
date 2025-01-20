import requests 
import os

# GitHub API
url = "https://api.github.com/users/ntando-mv15/repos"

def github_api():
    #Fetch data from API
    response = requests.get(url)

    data = response.json() 
    
    repo_file = os.getenv('FILE_PATH')
    
    # Iterate through the data 
    for repo in data:
        if status_code == 200:
            repo_name = repo["name"]
            with open(repo_file, "a") as new_file:    
                new_file.write(repo_name + "\n")
                print(f"Repository names saved to {file_path}")
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        
       
github_api()

