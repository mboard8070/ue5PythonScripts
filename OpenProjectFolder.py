import unreal
import os
import subprocess

def open_project_directory():
    project_dir = unreal.SystemLibrary.get_project_directory()
    print(project_dir)
    subprocess.run(['explorer', os.path.realpath(project_dir)])
    print('Completed')

open_project_directory()
