import unreal

# Set up the asset name and path
asset_name = "MeshPaint"
asset_path = "/Game/masterMaterials"

# Create a new material and set its properties
material_factory = unreal.MaterialFactoryNew()
material_asset = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
    asset_name, asset_path, unreal.Material, material_factory)

MaterialEditLibrary = unreal.MaterialEditingLibrary
MeshMaterial = unreal.load_asset(asset_path + '/' + asset_name)

# Add texture sample parameter nodes to the material
BaseColorParam = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300)
BaseColorParam.set_editor_property("parameter_name", "Base Color Texture")
BaseColorParam.set_editor_property("desc", "Base color texture parameter")

NormalParam = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300)
NormalParam.set_editor_property("parameter_name", "Normal Texture")
NormalParam.set_editor_property("desc", "Normal texture parameter")

OcclusionParam = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300)
OcclusionParam.set_editor_property("parameter_name", "Occlusion Texture")
OcclusionParam.set_editor_property("desc", "Occlusion texture parameter")

RoughnessParam = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300)
RoughnessParam.set_editor_property("parameter_name", "Roughness Texture")
RoughnessParam.set_editor_property("desc", "Roughness texture parameter")

MetallicParam = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300)
MetallicParam.set_editor_property("parameter_name", "Metallic Texture")
MetallicParam.set_editor_property("desc", "Metallic texture parameter")

# Add a vertex color node to blend the textures
vertex_color_node = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -384, -300)

# Create a lerp node for base color blending using the alpha channel of vertex color
lerp_base_color_node = MaterialEditLibrary.create_material_expression(
    MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -384, -300)
MaterialEditLibrary.connect_material_expressions(vertex_color_node, '', lerp_base_color_node, 'Alpha')
MaterialEditLibrary.connect_material_expressions(BaseColorParam, '', lerp_base_color_node, 'A')
MaterialEditLibrary.connect_material_expressions(unreal.LinearColor(0, 0, 0, 0), '', lerp_base_color_node, 'B')

# Connect the texture sample parameter nodes and lerp node to the material output
MaterialEditLibrary.connect_material_expressions(lerp_base_color_node, '', MeshMaterial, "Base Color")
MaterialEditLibrary.connect_material_expressions(NormalParam, '', MeshMaterial, "Normal")
MaterialEditLibrary.connect_material_expressions(OcclusionParam, '', MeshMaterial, "Ambient Occlusion")
MaterialEditLibrary.connect_material_expressions(RoughnessParam, '', MeshMaterial, "Roughness")
MaterialEditLibrary.connect_material_expressions(MetallicParam, '', MeshMaterial, "Metallic")

# Save the material asset
MeshMaterial.recompile_material()
unreal.EditorAssetLibrary.save_asset(MeshMaterial.get_path_name())





