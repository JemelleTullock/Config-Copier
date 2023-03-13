import os
import shutil
import time

os.system("title Config Copier")

source_items = [
    {
        'path': "C:/test/testdocument2.txt",
        'destination': "C:/test2"
    },
    {
        'path': "C:/test/testdocument2.txt",
        'destination': "C:/test3"
    },
    {
        'path': "//server/share/path/to/source/file1.ext",
        'destination': "C:/path/to/destination/directory1"
    },
    {
        'path': "//server/share/path/to/source/file2.ext",
        'destination': "C:/path/to/destination/directory2"
    }
]

for item in source_items:
    item_name = os.path.basename(item['path'])
    print(f"\033[32m{item_name}\033[0m ----> \033[32m{item['destination']}\033[0m")

overwrite_all = False
for item in source_items:
    
    item_name = os.path.basename(item['path'])

   
    dest_path = os.path.join(item['destination'], item_name)

  
    if not os.path.exists(item['path']):
        print(f"\033[31mError:\033[0m Source item \033[32m{item_name}\033[0m does not exist.")
        continue

    
    if not os.path.exists(item['destination']):
        print(f"\033[31mError:\033[0m Destination directory \033[32m{item['destination']}\033[0m does not exist.")
        continue

   
    while os.path.exists(dest_path):
        if not overwrite_all:
            overwrite = input(f"File/directory '\033[32m{item_name}\033[0m' already exists in '\033[32m{item['destination']}\033[0m'. Overwrite? (y/n/a): ")
            if overwrite.lower() == 'a':
                overwrite_all = True
                break
            elif overwrite.lower() != 'y':
                break

        if os.path.isdir(dest_path):
            shutil.rmtree(dest_path)
        else:
            os.remove(dest_path)

    if overwrite_all:
        print(f"Overwriting all existing files and directories in '\033[32m{item['destination']}\033[0m'.")

    
    try:
        if os.path.isdir(item['path']):
            shutil.copytree(item['path'], dest_path)
        else:
            shutil.copy(item['path'], dest_path)

    except PermissionError:
        print(f"\033[31mError:\033[0m You don't have sufficient network privileges to access {item['path']}.")
        continue


print("\033[32mFiles and folders copied successfully!\033[0m")


timer = 5
while timer > 0:
    print(f"\033[31mClosing in {timer} seconds...\033[0m")
    time.sleep(1)
    timer -= 1

