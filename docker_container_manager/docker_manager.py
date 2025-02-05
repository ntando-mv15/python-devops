

import docker 
from docker.errors import DockerException, APIError

def connect_to_docker():
    
    #Establishes a connection to the Docker daemon.
    #Returns a Docker client object if successful.
    try:
        client = docker.from_env()
        # Test the connection by pinging Docker daemon
        if client.ping():
            print("Connection to Docker successful!")
        return client
    except DockerException as e:
        print(f"Error connecting to Docker: {e}")
        return None         # If connection fails, return None 
 

def list_containers():
    
    try:
        client = connect_to_docker()
        # List all containers (including stopped ones) 
        container_list = client.containers.list(all=True)
        if not container_list:
            print("No containers found.")
        else:
            # List container details for each container
            for container in container_list:
                container_info = {}
                container_info["Container name"] = container.name
                container_info["Container ID"] = container.short_id
                container_info["Container Image"] = container.image.tags
                container_info["Container Status"] = container.status
                container_info["Container Uptime"] = container.attrs["State"]["StartedAt"]
                print(container_info)                
        return container_list
        
    except APIError as e:
        print(f"Error connecting to Docker: {e}")
        return None



list_containers()