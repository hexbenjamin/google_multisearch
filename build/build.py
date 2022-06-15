import json
import os
import PyInstaller.__main__
import zipfile


def build_exe():
    flags = [
        "replicant_search.py",
        "-n=replicant_search",
        "--onefile",
        "--console",
        "--distpath=/",
        "--workpath=/tmp"
    ]

    PyInstaller.__main__.run(flags)


build_dir = os.getcwd()
print(build_dir)
root_dir = os.path.dirname(build_dir)
print(root_dir)
excludes = os.path.join(build_dir, 'exclude.json')
print(excludes)

with open(excludes, 'r') as json_excludes:
    data = json.load(json_excludes)
    x_files = data["files"]
    x_dirs = data["dirs"]

print(x_files)
print(x_dirs)

print("let's build a Zipp !")
build_ver = input("version: replicant_search-r")
zip_name = 'replicant_search-r' + build_ver + '.zip'

if os.path.exists(zip_name):
    os.remove(zip_name)

zip_path = os.path.join(build_dir, zip_name)

# out_zip = zipfile.ZipFile(zip_path, 'w')

for dirname, subdirs, files in os.walk(root_dir):
    print(dirname)
    print(subdirs)
    print(files)
    print('---')
    
# out_zip.close()
