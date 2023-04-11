import unreal

#Access the current level
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()

# Spawn DirectionalLight actor
dir_light = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.DirectionalLight, unreal.Vector(0, 0, 300), unreal.Rotator(0, 0, 0)
)

dir_light.set_actor_label("sun_light")

# Find the Directional light
def find_dir_light_actor_by_label(label):
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    for actor in actors:
        if isinstance(actor, unreal.DirectionalLight) and actor.get_actor_label() == label:
            return actor
        return None
def set_directional_light_intensity(actor_label, intensity):
    directional_light_actor = find_dir_light_actor_by_label(actor_label)
    if directional_light_actor:
        directional_light_component = directional_light_actor.light_component
        directional_light_component.set_intensity(intensity)
        print(f"Directional Light intensity set to '{intensity}'")
    else:
        print(f"No Directional Light actor found with the name '{actor_label}'")

desired_intensity = 5000.0
directional_light_actor_label = "sun_light"
set_directional_light_intensity(directional_light_actor_label, desired_intensity)