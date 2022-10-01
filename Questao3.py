import os, json

directory = input("Directory name: ")

dictionary = {}
if os.path.isdir(directory):
    list_dir = os.listdir(directory)

    for i in list_dir:
        path = os.path.join(directory, i)
        if os.path.isfile(path):
            dictionary[i] = os.stat(path).st_size

    ordered_directories = {}
    for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
        ordered_directories[key] = str(value) + ' bytes'

    with open('list_directories.txt', 'w') as file:
        json.dump(ordered_directories, file, indent=4)
else:
    print("Directory", '\'' + directory + '\'', "does not exist.")
