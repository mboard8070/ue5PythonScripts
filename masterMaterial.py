import unreal

AssetMatTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditingLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary


masterMaterial = AssetMatTools.create_asset("masterMat", "/Game/Materials", unreal.Material, unreal.MaterialFactoryNew())

diffuseTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
diffuseTextureParameter.set_editor_property("Parameter_Name", "Color")
MaterialEditingLibrary.connect_material_property(diffuseTextureParameter, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

roughnessTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
roughnessTextureParameter.set_editor_property("Parameter_Name", "Roughness")
MaterialEditingLibrary.connect_material_property(roughnessTextureParameter, "RGB", unreal.MaterialProperty.MP_ROUGHNESS)

specScalarParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant, -125, 70)
specScalarParameter.set_editor_property('R', 0.2)
#specScalarParameter.set_editor_property("Parameter_Name", "Spec")
MaterialEditingLibrary.connect_material_property(specScalarParameter, "", unreal.MaterialProperty.MP_SPECULAR)

normalTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
normalTextureParameter.set_editor_property("Parameter_Name", "Normal")
normalTextureParameter.set_editor_property("SamplerType", "Normal")
MaterialEditingLibrary.connect_material_property(normalTextureParameter, "RGB", unreal.MaterialProperty.MP_NORMAL)

metalTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
metalTextureParameter.set_editor_property("Parameter_Name", "Metal")
MaterialEditingLibrary.connect_material_property(metalTextureParameter, "RGB", unreal.MaterialProperty.MP_METALLIC)

aOTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
aOTextureParameter.set_editor_property("Parameter_Name", "AO")
MaterialEditingLibrary.connect_material_property(aOTextureParameter, "RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

#Match Directory Path at top it isn't the same right now
#EditorAssetLibrary.save_asset("/Game/masterMaterials/M_Master", True)