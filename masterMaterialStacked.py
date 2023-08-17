import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

MasterMaterialStacked = AssetTools.create_asset("M_Master_Stacked", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
BaseColorTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, -300)
BaseColorTextureParam.set_editor_property("Parameter_Name", "Color")
MaterialEditLibrary.connect_material_property(BaseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create a Constant Value and Connect to Specular
SpecParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionConstant, -250, 70)
SpecParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(SpecParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create a 2D Texture Param and Connect to Normal
NormalTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, -200)
NormalTextureParam.set_editor_property("Parameter_Name", "Normal")
NormalTextureParam.set_editor_property("sampler_type", unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
MaterialEditLibrary.connect_material_property(NormalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Occlusion, Roughness and Metallic
OrmTextureParam = MaterialEditLibrary.create_material_expression(MasterMaterialStacked, unreal.MaterialExpressionTextureSampleParameter2D, -384, 100)
OrmTextureParam.set_editor_property("Parameter_Name", "ORM")
OrmTextureParam.set_editor_property("sampler_type", unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)
MaterialEditLibrary.connect_material_property(OrmTextureParam, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(OrmTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(OrmTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)

#Create Material Instance
StackedMatInstance = AssetTools.create_asset("MI_Stacked_Orm", "/Game/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(StackedMatInstance, MasterMaterialStacked)
StackedMatInstance.set_editor_property("Parent", MasterMaterialStacked)
MaterialEditLibrary.update_material_instance(StackedMatInstance)

EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_Master_Stacked")
EditorAssetLibrary.save_asset("/Game/MasterMaterials/MI_Stacked_Orm")
