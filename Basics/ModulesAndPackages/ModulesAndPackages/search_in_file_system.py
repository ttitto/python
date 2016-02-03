import sys
import os
from glob import glob

def print_if_present(list:list):
    if list:
        for element in list:
            print(element)
        return True
    else:
        return False


def find_file(initial_dir, filename_pattern):
    if not os.path.exists(initial_dir):
        print('Path {} not found'.format(initial_dir))
    else:
        file_found = False
        file_found = file_found or print_if_present(glob(os.path.join(initial_dir, filename_pattern)))
        for root, dirs, files in os.walk(initial_dir):
            for dir in dirs:
                file_found = file_found or print_if_present(glob(os.path.join(root, dir, filename_pattern)))
        if not file_found:
            print("File not found.")


if len(sys.argv) < 3:
    print('Please provide correct arguments')
else:
    find_file(initial_dir = sys.argv[1], filename_pattern = sys.argv[2])