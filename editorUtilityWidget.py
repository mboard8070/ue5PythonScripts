import unreal

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
widgetTools = unreal.WidgetLibrary
slateTools = unreal.SlateLibrary

editorSubSys = unreal.get_editor_subsystem(unreal.EditorSubsystem)


myWidget = assetTools. create_asset("chatGPTWidget", "/Game/pyWidgets", unreal.EditorUtilityWidgetBlueprint, unreal.EditorUtilityWidgetBlueprintFactory())

myButton = assetTools.create_asset("myButton", "/Game/pyWidgets", unreal.SlateLibrary, unreal.SlateBrushAssetFactory())





