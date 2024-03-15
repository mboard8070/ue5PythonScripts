import unreal

# Get the current editor world
editor_world = unreal.EditorLevelLibrary.get_editor_world()
#editor_world = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
#Get post process settings


# Define the location and rotation for the PostProcessVolume
location = unreal.Vector(0, 0, 0)
rotation = unreal.Rotator(0, 0, 0)

# Spawn the PostProcessVolume
post_process_volume = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PostProcessVolume.static_class(), location, rotation)

post_process_volume.unbound = True # Affect whole scene

# Disable autoexposure for more control
# NOTE: This just sets the values, you still need to activate these properties in the editor
# TODO: Figure out if this can be done from Python

settings = post_process_volume.

settings.bloom_intensity = 100.0
settings.auto_exposure_method = unreal.AutoExposureMethod.AEM_MANUAL
settings.auto_exposure_apply_physical_camera_exposure = False


#post_process_volume.set_editor_property('Bloom', unreal.PostProcessSettings.bloom_intensity, True)



#ppv.settings.set_editor_property("AutoExposureMethod", unreal.AutoExposureMethod.AEM_MANUAL, unreal.PropertyAccessChangeNotifyMode.ALWAYS)