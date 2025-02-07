# Main Script to Run Functions 

from docker_operations import connect_to_docker, list_containers, start_container, stop_container

def main():
    client = connect_to_docker()
    if not client:
        return  # Exit if connection fails
    
    while True:
        print("\nDocker Container Manager:")
        
        print("1. List all containers")
        print("2. Start a stopped container")
        print("3. Stop a running container")
        print("4. Exit Docker Container Manager")
        print(" ")
        

        user_choice = input("Please enter your choice (1-4): ")

        if user_choice == "1":
            list_containers(client)
        elif user_choice == "2":
            start_container(client)
        elif user_choice == "3":
            stop_container(client)
        elif user_choice == "4":
            print("\nExiting Docker Manager. Goodbye!") 
        else:
            print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()