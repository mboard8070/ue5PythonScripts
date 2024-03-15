import unreal

# Get the current editor world
editor_world = unreal.EditorLevelLibrary.get_editor_world()

# Define the location and rotation for the PostProcessVolume
location = unreal.Vector(0, 0, 0)
rotation = unreal.Rotator(0, 0, 0)

# Spawn the PostProcessVolume
post_process_volume = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PostProcessVolume.static_class(), location, rotation)

post_process_volume.unbound = True  # Affect whole scene

# Access the post process settings of the volume
settings = post_process_volume.get_editor_property("PostProcessSettings")

# Modify the settings
settings.bloom_intensity = 1.0  # Set your desired value here
settings.auto_exposure_method = unreal.AutoExposureMethod.AEM_MANUAL
settings.auto_exposure_apply_physical_camera_exposure = False

# Apply the modified settings back to the volume
post_process_volume.set_editor_property("PostProcessSettings", settings)
