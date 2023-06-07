import os

file_path = '/users/jondoe/Downloads' # Your location of the file with the files name with extension

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted!")
else:
    print("This file does not exist!!!")