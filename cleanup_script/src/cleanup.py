import os 
import logging

log_dir = "/mnt/c/Users/NTAND/cleanup_project/logs" 



# create some txt files in dir

for number in range(1, 4):
    filename = f"log{number}.txt" 
    if os.path.exists(os.path.join(log_dir, filename)):
        print(f"File {filename} already exists")
    else:
        with open(os.path.join(log_dir, filename), "w") as newfile:
            pass
        print(f"File {filename} successfully created")
        
        
# create .tmp files       
for number in range(1, 7):
    filename = f"temp{number}.tmp" 
    if os.path.exists(os.path.join(log_dir, filename)):
        print(f"File {filename} already exists")
    else:
        with open(os.path.join(log_dir, filename), "w") as newfile:
            pass
        print(f"File {filename} successfully created")
    
list_dir = os.listdir(log_dir)
print("Before cleanup:", list_dir) 

# find .tmp files specifically in logs dir 
log_file = os.path.join(log_dir, "script.log")
logging.basicConfig(filename=log_file, level=logging.INFO)

for file in os.listdir(log_dir):
    if file.endswith(".tmp"): 
        file_path = os.path.join(log_dir, file)
        os.remove(file_path)
        if os.path.exists(file_path):
            print(f"File {file_path} deletion unsuccessful.")
            logging.error(f"File {file_path} not deleted.")
        else:
            print(f"File {file_path} deletion successful.")
            logging.info(f"File {file_path} deleted.")

list_dir = os.listdir(log_dir)
print("After cleanup:", list_dir)

