import unreal
import os

# instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Directory mapping
Directory_mapping = {
    "ActorComponent": "\\Game\\Blueprints\\Components\\",
    "AnimationBlueprint": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "AnimationSequence": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "AnimBlueprint": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "AnimMontage": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "AnimSequence": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "BehaviorTree": "\\Game\\AI\\",
    "BlackboardData": "\\Game\\AI\\",
    "BlendSpace": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "BlendSpace1D": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "Blueprint": "\\Game\\Blueprints\\",
    "BlueprintInterface": "\\Game\\Blueprints\\",
    "ControlRigBlueprint": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "CurveFloat": "\\Game\\Blueprints\\Data\\",
    "CurveLinearColor": "\\Game\\Blueprints\\Data\\",
    "CurveLinearColorAtlas": "\\Game\\Blueprints\\Data\\",
    "CurveTable": "\\Game\\Blueprints\\Data\\",
    "DataTable": "\\Game\\Blueprints\\Data\\",
    "EditorUtilityBlueprint": "\\Game\\Tools\\",
    "EditorUtilityWidgetBlueprint": "\\Game\\Tools\\",
    "Enum": "\\Game\\Blueprints\\Data\\",
    "EnvQuery": "\\Game\\AI\\",
    "HDRI": "\\Game\\Other\\",
    "IKRetargeter": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "IKRigDefinition": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "LevelSequence": "\\Game\\Other\\",
    "LevelSnapshots": "\\Game\\Other\\",
    "Material": "\\Game\\Materials\\",
    "MaterialFunction": "\\Game\\Materials\\Functions\\",
    "MaterialFunctionMaterialLayer": "\\Game\\Materials\\Functions\\",
    "MaterialInstance": "\\Game\\Materials\\Instances\\",
    "MaterialInstanceConstant": "\\Game\\Materials\\Functions\\",
    "MaterialParameterCollection": "\\Game\\Materials\\Functions\\",
    "MediaOutput": "\\Game\\Media\\",
    "MediaPlayer": "\\Game\\Media\\",
    "MediaProfile": "\\Game\\Media\\",
    "MediaSource": "\\Game\\Media\\",
    "MediaTexture": "\\Game\\Media\\",
    "Montages": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "MorphTarget": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "NDisplayConfiguration": "\\Game\\Other\\",
    "NiagaraEmitter": "\\Game\\FX\\Emitters\\",
    "NiagaraFunction": "\\Game\\FX\\Functions\\",
    "NiagaraSystem": "\\Game\\FX\\",
    "OCIOProfile": "\\Game\\Other\\",
    "ParticleSystem": "\\Game\\FX\\",
    "PhysicsAsset": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "PhysicsMaterial": "\\Game\\Materials\\",
    "PoseAsset": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "PostProcessMaterial": "\\Game\\Materials\\",
    "RemoteControlPreset": "\\Game\\Tools\\",
    "RenderTarget": "\\Game\\Materials\\Textures\\",
    "Rig": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "SequencerEdits": "\\Game\\Meshes\\SkeletalMeshes\\Animations\\",
    "SkeletalMesh": "\\Game\\Meshes\\SkeletalMeshes\\",
    "Skeleton": "\\Game\\Meshes\\SkeletalMeshes\\",
    "SoundCue": "\\Game\\Media\\Sounds\\\\",
    "SoundWave": "\\Game\\Media\\Sounds\\\\",
    "StaticMesh": "\\Game\\Meshes\\",
    "Structure": "\\Game\\Blueprints\\Data\\",
    "Texture2D": "\\Game\\Materials\\Textures\\",
    "TextureCube": "\\Game\\Materials\\Textures\\",
    "TextureRenderTarget2D": "\\Game\\Materials\\Textures\\",
    "UserDefinedEnum": "\\Game\\Blueprints\\Data\\",
    "UserDefinedStruct": "\\Game\\Blueprints\\Data\\",
    "WidgetBlueprint": "\\Game\\UMG\\",
    "World": "\\Game\\Maps\\"
}

# get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
cleaned = 0

# hard coded parent directory
parent_dir = "\\Game"

for asset in selected_assets:
    # get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)
    Move_to_directory = Directory_mapping.get(class_name, None)

    # Assemble path to relocate assets
    try:
        new_path = Move_to_directory + asset_name
        # new_path = os.path.join(parent_dir, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1
        unreal.log("Cleaned up {} to {}".format(asset_name, new_path))
    # unreal.log(join(parent_dir, class_name, asset_name))

    except Exception as err:
        unreal.log("Could not move {} to new location {}".format(asset_name, new_path))

    unreal.log("Asset {} with the class {}".format(asset_name, class_name))

unreal.log("Cleaned up {} of {} assets".format(cleaned, num_assets))