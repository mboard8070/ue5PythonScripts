import unreal
import os

def importMyAssets():
	path = os.path.join(unreal.SystemLibrary.get_project_directory(), os.pardir, 'FBXImportDirectory')

	for filename in os.listdir(path):
		full_filename = os.path.join(path, filename)
		print(full_filename)
		if os.path.isfile(full_filename) and filename.lower().endswith('.fbx'):
			Static_mesh_task = buildImportTask(full_filename, '/Game/Meshes', buildStaticMeshImportOptions())
			executeImportTasks([Static_mesh_task])

def buildImportTask(filename, destination_path, options=None):
	task = unreal.AssetImportTask()
	task.set_editor_property('automated',True)
	task.set_editor_property('destination_name', '')
	task.set_editor_property('destination_path', destination_path)
	task.set_editor_property('filename', filename)
	task.set_editor_property('replace_existing', False)
	task.set_editor_property('save',True)
	task.set_editor_property('options', options)
	return task

def buildStaticMeshImportOptions():
	options = unreal.FbxImportUI()

	options.set_editor_property('import_mesh', True)
	options.set_editor_property('import_textures', False)
	options.set_editor_property('import_materials', True)
	options.set_editor_property('import_as_skeletal', False)

	options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(50.0, 0.0, 0.0))
	options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 110.0, 0.0))
	options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

	options.static_mesh_import_data.set_editor_property('combine_meshes', True)
	options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
	options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
	return options


def executeImportTasks(tasks):
	unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

importMyAssets()
