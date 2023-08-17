import unreal

# Ensure that you're using the correct factory classes and API functions.
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create or retrieve the Editor Utility Widget.
widget_path = "/Game/pyWidgets/EUW_Widget"
editor_utility_widget_class = unreal.EditorUtilityWidgetBlueprint
editor_utility_widget_factory_class = unreal.EditorUtilityWidgetBlueprintFactory

# Check if widget exists, if not, create one
existing_widget = unreal.EditorAssetLibrary.load_asset(widget_path)
if not existing_widget:
    my_widget = asset_tools.create_asset("EUW_Widget", "/Game/pyWidgets", editor_utility_widget_class, editor_utility_widget_factory_class())

# Saving the asset (This step is crucial)
unreal.EditorAssetLibrary.save_asset(widget_path)


