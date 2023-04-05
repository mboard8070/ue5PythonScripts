import unreal

actorLocation = unreal.Vector(0, 0, 0)

pointLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PointLight, actorLocation)

pointLight.set_actor_label("key_light")