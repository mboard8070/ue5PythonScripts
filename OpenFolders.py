import unreal
import os
import subprocess

def openCodeFolder():
	pythondir = os.path.join(unreal.SystemLibrary.get_project_directory(), os.pardir, 'PythonCode')
	print(pythondir)
	#subprocess.Popen(r'explorer /select, os.path.join(unreal.SystemLibrary.get_project_directory(), os.pardir, 'PythonCode')')
	os.popen(pythondir)
	print('Completed')
	#subprocess.Popen(r'explorer /select, "E:"')
	#subprocess.Popen(r'explorer /select,"C:\\"')
	subprocess.run(['explorer', os.path.realpath(pythondir)])

openCodeFolder()