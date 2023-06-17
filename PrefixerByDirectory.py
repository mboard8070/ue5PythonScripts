import unreal
import json

# instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# prefix mapping
prefix_mapping = {
    "ActorComponent": "AC_",
    "AnimationBlueprint": "ABP_",
    "AnimationSequence": "AS_",
    "AnimBlueprint": "ABP_",
    "AnimMontage": "AMON_",
    "AnimSequence": "ASEQ_",
    "BehaviorTree": "BT_",
    "BlackboardData": "BB_",
    "BlendSpace": "BS_",
    "BlendSpace1D": "BS_",
    "Blueprint": "BP_",
    "BlueprintInterface": "BI_",
    "ControlRigBlueprint": "CTRIG_",
    "CurveFloat": "CURV_",
    "CurveLinearColor": "CURV_",
    "CurveLinearColorAtlas": "CURV_",
    "CurveTable": "CT_",
    "DataTable": "DT_",
    "EditorUtilityBlueprint": "EU_",
    "EditorUtilityWidgetBlueprint": "EUW_",
    "Enum": "E_",
    "EnvQuery": "EQ_",
    "HDRI": "HDR_",
    "IKRetargeter": "IKRT_",
    "IKRigDefinition": "IKRIG_",
    "LevelSequence": "LS_",
    "LevelSnapshots": "SNAP_",
    "Material": "M_",
    "MaterialFunction": "MF_",
    "MaterialFunctionMaterialLayer": "MFL_",
    "MaterialInstance": "MI_",
    "MaterialInstanceConstant": "MI_",
    "MaterialParameterCollection": "MPC_",
    "MediaOutput": "MO_",
    "MediaPlayer": "MP_",
    "MediaProfile": "MPR_",
    "MediaSource": "MS_",
    "MediaTexture": "MEDT_",
    "Montages": "AM_",
    "MorphTarget": "MT_",
    "NDisplayConfiguration": "NDC_",
    "NiagaraEmitter": "FXE_",
    "NiagaraFunction": "FXF_",
    "NiagaraSystem": "FXS_",
    "OCIOProfile": "OCIO_",
    "ParticleSystem": "PS_",
    "PhysicsAsset": "PHYS_",
    "PhysicsMaterial": "PM_",
    "PoseAsset": "POSEA_",
    "PostProcessMaterial": "PPM_",
    "RemoteControlPreset": "RCP_",
    "RenderTarget": "RT_",
    "Rig": "RIG_",
    "SequencerEdits": "EDIT_",
    "SkeletalMesh": "SK_",
    "Skeleton": "SKEL_",
    "SoundCue": "SC_",
    "SoundWave": "S_",
    "StaticMesh": "SM_",
    "Structure": "F_",
    "Texture2D": "T_",
    "TextureCube": "TCUB_",
    "TextureRenderTarget2D": "TRT_",
    "UserDefinedEnum": "E_",
    "UserDefinedStruct": "STRUCT_",
    "WidgetBlueprint": "WBP_",
    "World": "LVL_"
}
#with open(".\\prefix_mapping.json", "r") as json_file:
#    prefix_mapping = json.loads(json_file.read())

def runprefixer():
    # get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    prefixed = 0

    for asset in selected_assets:
        # get the class instance and the clear text name
        asset_name = system_lib.get_object_name(asset)
        asset_class = asset.get_class()
        class_name = system_lib.get_class_display_name(asset_class)

        # get the prefix for the given class
        class_prefix = prefix_mapping.get(class_name, None)

        if class_prefix is None:
            unreal.log_warning("No mapping for asset {} of type {}".format(asset_name, class_name))
            continue

        if not asset_name.startswith(class_prefix):
            # rename the asset and add prefix
            new_name = class_prefix + asset_name
            editor_util.rename_asset(asset, new_name)
            prefixed += 1
            unreal.log("Prefixed {} of type {} with {}".format(asset_name, class_name, class_prefix))

        else:
            unreal.log("Asset {} of type {} is already prefixed with {}".format(asset_name, class_name, class_prefix))

    unreal.log("Prefixed {} of {} assets".format(prefixed, num_assets))