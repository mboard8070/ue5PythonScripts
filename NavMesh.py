import unreal

# Get the current editor world
editor_world = unreal.EditorLevelLibrary.get_editor_world()

# Define the location and rotation for the NavMeshBoundsVolume
location = unreal.Vector(0, 0, 0)
rotation = unreal.Rotator(0, 0, 0)

# Spawn the NavMeshBoundsVolume
nav_mesh_volume = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.NavMeshBoundsVolume.static_class(), location, rotation)

# Set the mobility of the root component to movable
#nav_mesh_volume.RootComponent.set_mobility(unreal.ComponentMobility.MOVABLE)
nav_mesh_volume.root_component.set_mobility(unreal.ComponentMobility.MOVABLE)

# Optionally, you can set the size of the volume
nav_mesh_volume.set_actor_scale3d(unreal.Vector(10, 10, 10))
