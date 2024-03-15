import unreal

asset = unreal.EditorAssetLibrary.load_asset("/Game/Utilities/EUW_Python")

# Get the EditorUtilitySubsystem
Subsys = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)

# Spawn a new tab and register it with the EditorUtilitySubsystem
Subsys.spawn_and_register_tab(asset)