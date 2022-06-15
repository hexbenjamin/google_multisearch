import json
import os
from pathlib import Path
import PyInstaller.__main__
import zipfile


def build_exe():
    flags = [
        "replicant_search.py",
        "-n=replicant_search",
        "--onefile",
        "--console",
        "--distpath=/DEV/python/replicant_search",
        "--workpath=/DEV/python/replicant_search/tmp"
    ]

    PyInstaller.__main__.run(flags)

root_dir = os.getcwd()
build_dir = os.path.join(root_dir, 'build')
includes = os.path.join(build_dir, 'include.json')

build_exe()

os.chdir(build_dir)

with open(includes, 'r') as json_includes:
    data = json.load(json_includes)
    inc_files = data["include"]["files"]
    inc_dirs = data["include"]["dirs"]
    exc_files = data["exclude"]["files"]
    exc_dirs = data["exclude"]["dirs"]

print("let's build a Zipp !")
build_ver = input("version: replicant_search-r")
zip_name = 'replicant_search-r' + build_ver + '.zip'

if os.path.exists(zip_name):
    os.remove(zip_name)

zip_path = os.path.join(build_dir, zip_name)

root_path = Path(root_dir)

with zipfile.ZipFile(zip_path, mode='w') as archive:
    for path in root_path.rglob("*"):
        rel_path = os.path.relpath(path, root_path)
        target_path = os.path.join("r_search", rel_path)
        if path.name in inc_files and path.name not in exc_files:
            archive.write(
                path,
                arcname=rel_path
            )
        elif path.parent.name in inc_dirs and path.parent.name not in exc_dirs:
            archive.write(
                path,
                arcname=rel_path
            )
    archive.close()