import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

masterMaterialStacked = AssetTools.create_asset("M_Master_Stacked", "/Game/masterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, -300)
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create Constant Value and Connect to Specular
specParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionConstant, -250, 70)
specParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(specParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, -200)
MaterialEditLibrary.connect_material_property(normalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Occlusion, Roughness, and Metallic
ormTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, 100)
MaterialEditLibrary.connect_material_property(ormTextureParam, "R",  unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ormTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ormTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)
ormTextureParam.rename("ORM")

#Create Material Instance
stackedMatInstance = AssetTools.create_asset("masterMatStacked_ORM_Inst", "/Game/masterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(stackedMatInstance, masterMaterialStacked)
stackedMatInstance.set_editor_property("Parent", masterMaterialStacked)
MaterialEditLibrary.update_material_instance(stackedMatInstance)


EditorAssetLibrary.save_asset("/Game/masterMaterials/M_Master_Stacked", True)
EditorAssetLibrary.save_asset("/Game/masterMaterials/masterMatStacked_ORM_Inst", True)