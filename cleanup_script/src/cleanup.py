import os 
import logging

log_dir = "/mnt/c/Users/NTAND/cleanup_project/logs" 
log_file = os.path.join(log_dir, "script.log")

# Setup logging
os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists
logging.basicConfig(filename=log_file, level=logging.INFO)


# Create .txt and .tmp files 
def create_file(directory, name, count, file_ext):
    # Create files in specific directory
    for number in range(1, count + 1):
        filename = f"{name}{number}{file_ext}"
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as newfile:
                pass
            print(f"File {filename} successfully created")
        else:
            print(f"File {filename} already exists")
            


def cleanup_tmp_files():
    # Delete .tmp files in specific directory
    for file in os.listdir(log_dir):
        if file.endswith(".tmp"):
            file_path = os.path.join(log_dir, file)
            try: 
                os.remove(file_path)
                logging.info(f"File {file_path} deleted.")
                print(f"File {file_path} deletion successful.")
            except Exception as e:
                logging.info(f"Error deleting file {file_path}: {e}")
                print(f"Error deleting file {file_path}: {e}")



def main():
    print(f"Logs directory: {log_dir}")
    
    # Create files
    create_file(log_dir, "temp", 6, ".tmp")
    create_file(log_dir, "log", 3, ".txt")
    
    list_dir = os.listdir(log_dir)
    print("Before cleanup:", list_dir)
    
    # Cleanup .tmp files
    cleanup_tmp_files()
    
    # List files before cleanup
    list_dir = os.listdir(log_dir)
    print("After cleanup:", list_dir) 

if __name__ == "__main__":
    main()