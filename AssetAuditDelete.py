import unreal

# Collect all assets in the project
all_assets = unreal.EditorAssetLibrary.list_assets("/Game")

# Initialize an empty set to hold assets used in levels
used_assets = set()

# For each level in the project
for level_path in unreal.EditorAssetLibrary.list_assets("/Game/Maps"):
    # Load the level
    level = unreal.EditorAssetLibrary.load_asset(level_path)

    # For each actor in the level
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        # For each asset referenced by the actor
        for asset_path in unreal.EditorAssetLibrary.list_referenced_assets(actor.get_path_name()):
            # Add the asset to the used assets set
            used_assets.add(asset_path)

# For each asset in the project
for asset_path in all_assets:
    # If the asset is not used in any level
    if asset_path not in used_assets:
        # Delete the asset
        unreal.EditorAssetLibrary.delete_asset(asset_path)
