import docker 
from docker.errors import DockerException, APIError, NotFound 

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
        # List all containers (including stopped ones) 
        container_list = client.containers.list(all=True)
        if not container_list:
            print("No containers found.")
        else:
            # List container details for each container
            for container in container_list:
                print(f"Container name: {container.name}, Container ID: {container.short_id}, Container Image: {container.image.tags}, Container Status: {container.status}, Container Uptime: {container.attrs['State']['StartedAt']}")
                                      
    except APIError as e:
        print(f"Error listing containers: {e}")
        return None

def start_container():
    
    try:
        
        stopped_containers = client.containers.list(filters={"status": "exited"})
        
        # Ask user which container they would like to start
        user_input = input("Please enter the container ID to restart: ")
        
        container_id = client.containers.get(user_container)
        
        if not container_id in stopped_containers:
            print("No container found.")
            
        container_id.start()
        print("Container {container_id} successfully started.")
        
        # Check if container restarted and is running
        running_containers = client.containers.list()
        print(running_containers)
            
    except NotFound as e:
        print(f"Error fetching container: {e}")   
    
def stop_container(client):
    
    try:
        
        running_containers = client.containers.list(filters={"status": "running"})
        
        # Ask user which container they would like to stop
        user_container = input("Please enter the container ID to stop: ")
        
        container_id = client.containers.get(user_container)
        
        if not container_id in running_containers:
            print("No container found.")
            
        container_id.stop()
        print("Container successfully stopped.")
        
        # Check if container is running
        stopped_containers = client.containers.list(filters={"status": "stopped"})
        print(stopped_containers)
            
    except (NotFound, APIError) as e:
        print(f"Error fetching container: {e}")
      

