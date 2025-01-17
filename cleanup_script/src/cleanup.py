import os 
import logging

log_dir = "/mnt/c/Users/NTAND/cleanup_project/logs" 
log_file = os.path.join(log_dir, "script.log")


# Create .txt and .tmp files 
def create_file(directory, name, count, file_ext):
    for number in range(1, count + 1):
        filename = f"{name}{number}{file_ext}"
        if not os.path.exists(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), "w") as newfile:
                pass
            print(f"File {filename} successfully created")
        else:
            print(f"File {filename} already exists")
            
            
    
list_dir = os.listdir(log_dir)
print("Before cleanup:", list_dir) 

# Set up logging 
logging.basicConfig(filename=log_file, level=logging.INFO)


def cleanup_tmp_files():
    # Delete .tmp files in specified directory
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

list_dir = os.listdir(log_dir)
print("After cleanup:", list_dir)

def main():
    create_file(log_dir, "temp", 6, ".tmp")
    create_file(log_dir, "log", 3, ".txt")
    
    
    
    
    
    

if __name__ == "__main__":
    main()