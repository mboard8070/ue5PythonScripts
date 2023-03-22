import unreal

AssetMatTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditingLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary


masterMaterial = AssetMatTools.create_asset("masterMatStacked_ORM", "/Game/Materials", unreal.Material, unreal.MaterialFactoryNew())

#Texture Parameter
diffuseTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
#Connect to Material Channel
MaterialEditingLibrary.connect_material_property(diffuseTextureParameter, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

specParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant, -125, 70)
specParameter.set_editor_property('R', 0.2)
MaterialEditingLibrary.connect_material_property(specParameter, "", unreal.MaterialProperty.MP_SPECULAR)

normalTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
MaterialEditingLibrary.connect_material_property(normalTextureParameter, "RGB", unreal.MaterialProperty.MP_NORMAL)

ormTextureParameter = MaterialEditingLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, 100)
MaterialEditingLibrary.connect_material_property(ormTextureParameter, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditingLibrary.connect_material_property(ormTextureParameter, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditingLibrary.connect_material_property(ormTextureParameter, "B", unreal.MaterialProperty.MP_METALLIC)

#create material instance
masterMaterialInstance = AssetMatTools.create_asset("masterMatStacked_ORM_Inst", "/Game/Materials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

