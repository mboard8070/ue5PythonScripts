import unreal

# instances of unreal classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# get all actors and then filter them by class or name
actors = editor_level_lib.get_all_level_actors()
static_meshes = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
blueprints = editor_filter_lib.by_id_name(actors, "BP_")
#extra classes could be added here
count = 0


# create a mapping between folder names and actors
mapping = {
	"StaticMeshes": static_meshes,
	"Blueprints": blueprints
	#Extra Items could be added here
}

for folder in mapping:
	# Loop through each actor and place them in folders
	for actor in mapping[folder]:
		actor_name = actor.get_fname()
		actor.set_folder_path(folder)
		unreal.log("Moved {} into {}".format(actor_name, folder))

		count += 1


unreal.log("Moved {} actors moved".format(count))
