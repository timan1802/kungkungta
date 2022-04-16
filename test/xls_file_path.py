import os

xls_dir_path = "../dict_xls"

for (root, directories, files) in os.walk(xls_dir_path):
    for file in files:
        if '.xls' in file:
            xls_file_path = os.path.join(root, file)
            print(xls_file_path)