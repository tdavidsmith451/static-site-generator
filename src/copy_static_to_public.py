import os
import shutil

def copy_static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")

#def copy_dirs(source, dest):
#    for file in os.listdir(source):
#        file_path = f"{source}/{file}"
#        if os.path.isfile(file_path):
#            shutil.copy(file_path, dest)
#        if os.path.isdir(file_path):
            #copy_dirs()