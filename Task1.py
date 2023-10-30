import sys
import os

def print_version():
    print("Python Version:")
    print(sys.version)

def create_directory(directory_name):
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")

def list_files_and_folders():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    print(f"Files and folders in the parent directory '{parent_dir}':")
    for item in os.listdir(parent_dir):
        item_path = os.path.join(parent_dir, item)
        if os.path.isdir(item_path):
            print(item)
        else:
            print(f"File: {item}")


while True:
    command = int(input("Enter:\n1-Print version\n2-Create directory\n3-Print a list of files and folders\n0-Exit"))
    if command == 1:
        print_version()
    elif command==2:
        name = input("Write name")
        create_directory(name)
    elif command==3:
        list_files_and_folders()
    elif command==0:
        break
    else:
        print("wrong command")


