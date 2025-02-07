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
 

def list_containers(client):
    
    try:
        # List all containers (both running and stopped ones) 
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

def start_container(client):
    # Function allows user to start a stopped container
    try:
        
        stopped_containers = client.containers.list(filters={"status": "exited"})
        
        # Prompts user to start a specific stopped container
        user_input = input("Please enter the ID of a stopped container to start (Check list of containers for the ID): ")
        
        container = client.containers.get(user_input)
        
        if not container in stopped_containers:
            print("No container found.")
            
        else:
            container.start()
            print("Container successfully started.")
        
            # Refresh the container's status
            container.reload()
        
            # Check if container restarted and is running
            is_running = container.status
            print(f"Container {container.name} is now {is_running}")
            
    except NotFound as e:
        print(f"Container not found with ID '{user_input}'. Please verify the ID and try again.")  
    except APIError as e:
        print(f"API error occurred while starting the container: {e}")   
    
def stop_container(client):
    # Fucntion allows user to stop a running container
    try:
        
        running_containers = client.containers.list(filters={"status": "running"})
        
        # Ask user which container they would like to stop
        user_input = input("Please enter the ID of the running container to stop (Check list of containers for the ID): ")
        
        container = client.containers.get(user_input)
        
        if not container in running_containers:
            print("No container found.")
        else:    
            container.stop()
            print("Container successfully stopped.")
        
            # Refresh the container's status
            container.reload()
        
            # Check if container is running
            is_stopped = container.status
            print(f"Container {container.name} is now {is_stopped}")
            
    except NotFound as e:
        print(f"Container not found with ID '{user_input}'. Please verify the ID and try again.")  
    except APIError as e:
        print(f"API error occurred while starting the container: {e}") 
      

