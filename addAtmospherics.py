import unreal



#This script adds all atmosphere related actors to a scene
actorLocation = unreal.Vector(0, 0, 0)
actorRotation = unreal.Rotator(0, 0, 0)
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)



# create a new atmosphereic actors
dirLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, actorLocation)
skyLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, actorLocation)
sky = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyAtmosphere, actorLocation)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.ExponentialHeightFog, actorLocation)
# set the actor's rotation
#dirLight.set_actor_rotation(actorRotation, False)

# add the actor to the level
#unreal.EditorLevelLibrary.add_actor_to_level(dirLight, unreal.EditorLevelLibrary.get_editor_world())
levelSubSys.save_current_level()

