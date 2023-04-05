import unreal

actorLocation = unreal.Vector(0, 0, 0)

pointLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PointLight, actorLocation)

pointLight.set_actor_label("key_light")


# Function to find the first point light actor in the scene
def find_point_light_actor_by_label(label):
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    for actor in actors:
        if isinstance(actor, unreal.PointLight) and actor.get_actor_label() == label:
            return actor
    return None

# Set the intensity of the point light
def set_point_light_intensity(actor_label, intensity):
    point_light_actor = find_point_light_actor_by_label(actor_label)
    if point_light_actor:
        point_light_component = point_light_actor.light_component
        point_light_component.set_intensity(intensity)
        print(f"Point light intensity set to '{intensity}'")
    else:
        print(f"No PointLight actor found with the name '{actor_label}'")

# Set the desired intensity value
desired_intensity = 1000.0
point_light_actor_label = "key_light"
set_point_light_intensity(point_light_actor_label, desired_intensity)
