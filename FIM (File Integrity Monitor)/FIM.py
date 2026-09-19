import os
from datetime import datetime
import time
import hashlib

#github: https://github.com/zxcresp

#============ASK USER TO SELECT DIRECTORY FOR MONITORING============
directory = input('Enter a directory to check: ')
report = input('Enter location where you want to save the report: ')
if not os.path.isdir(directory):
    print("Directory does not exist")
    exit()
#elif os.path.isdir(directory):
#    print('Directory exists')

#============FUNC============

def get_files(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths

def calculate_file_hash(filepath):
    hash_sha512 = hashlib.sha512()

    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hash_sha512.update(chunk)

        return hash_sha512.hexdigest()

    except (FileNotFoundError, PermissionError):
        return None

def create_baseline(files):
    baseline = {}

    for file in files:
        file_hash = calculate_file_hash(file)

        if file_hash is not None:
            baseline[file] = file_hash

    return baseline

def compare_baselines(old, new):
    for file in new:
        if file not in old:
            print(f'NEW: {file}')
        elif new[file] != old[file]:
            print(f'MODIFIED: {file}')
    for file in old:
        if file not in new:
            print(f'DELETED: {file}')

files = get_files(directory)
baseline = create_baseline(files)

while True:
    #You can keep this line or not. If you comment it out, CPU usage will be high, but changes in the directory will appear without a 5-second delay. If you uncomment it, CPU load will drop.
    #time.sleep(5)

    current_files = get_files(directory)
    current_baseline = create_baseline(current_files)

    compare_baselines(baseline, current_baseline)

    baseline = current_baseline
#============THIS PIECE OF CODE NECESSARY TO BE CHECKED============
#for file, file_hash in baseline.items():
#    print(file)
#    print(file_hash)