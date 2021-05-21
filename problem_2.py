import os

def file_finder(suffix, path):
    return find_files(suffix, path,[])
def find_files(suffix, path,subfolders):

    for paths in os.listdir(path): 
        join_path=os.path.join(path,paths)
        if join_path.endswith(suffix):
            subfolders.append(join_path)
        elif os.path.isdir(join_path):
            find_files(suffix, join_path,subfolders)
    return subfolders


print(file_finder(".c", os.getcwd()))
print(file_finder(".z", os.getcwd()))
print(file_finder(".h", os.getcwd()))
print(file_finder(".none", os.getcwd()))
print(file_finder("ex.py", os.getcwd()))