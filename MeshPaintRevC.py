import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

MeshMaterial = AssetTools.create_asset("M_MeshPaint", "/Game/masterMaterials", unreal.Material, unreal.MaterialFactoryNew())

# Add texture parameter nodes for each surface
base_colors = []
normals = []
orms = []

# Create a Vertex Color node
VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -500, -300)
VertexColorNode_Color.set_editor_property('Desc', 'Vertex Color Base_Color')
VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -500, -400)
VertexColorNode_Normal.set_editor_property('Desc', 'Vertex Color Normal')

# Create a Vertex Color node for each ORM channel
VertexColorNode_ORM_R = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -500, -150)
VertexColorNode_ORM_R.set_editor_property('Desc', 'Vertex Color ORM_R')
VertexColorNode_ORM_G = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -500, 0)
VertexColorNode_ORM_G.set_editor_property('Desc', 'Vertex Color ORM_G')
VertexColorNode_ORM_B = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), -500, 150)
VertexColorNode_ORM_B.set_editor_property('Desc', 'VertexColor ORM_B')

# Create a 1-x nodes for each channel so that the textures from 5 to 1 can loop
OneMinusNodeColor = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionOneMinus.static_class(), 0, -300)
OneMinusNodeNormal = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionOneMinus.static_class(), 0, -400)
OneMinusNode_R = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionOneMinus.static_class(), 0, -500)
OneMinusNode_G = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionOneMinus.static_class(), 0, -600)
OneMinusNode_B = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionOneMinus.static_class(), 0, -600)

for i in range(5):
    # Create base color, normal, and ORM texture parameter nodes
    BaseColorParam = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384, -300 + i * 150)
    NormalParam = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384 + 300, -300 + i * 150)
    OrmParam = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), -384 + 600, -300 + i * 150)

    # Set names and other properties for the nodes
    BaseColorParam.set_editor_property("ParameterName", unreal.Name("BaseColor_{}".format(i)))
    BaseColorParam.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParam.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    NormalParam.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParam.set_editor_property('sampler_type', unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
    OrmParam.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))
    OrmParam.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    OrmParam.set_editor_property('sampler_type', unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)

    base_colors.append(BaseColorParam)
    normals.append(NormalParam)
    orms.append(OrmParam)

# Create lerp nodes for the base color, normals, and orms
base_color_lerps = []
normal_lerps = []
orm_r_lerps = []
orm_g_lerps = []
orm_b_lerps = []

for i in range(5):
    base_color_lerp = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -192, -300 + i * 150)
    normal_lerp = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -192 + 300, -300 + i * 150)
    orm_r_lerp = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -192 + 600, -300 + i * 150)
    orm_g_lerp = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -192 + 600, -300 + i * 150 + 200)
    orm_b_lerp = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), -192 + 600, -300 + i * 150 + 400)

    base_color_lerps.append(base_color_lerp)
    normal_lerps.append(normal_lerp)
    orm_r_lerps.append(orm_r_lerp)
    orm_g_lerps.append(orm_g_lerp)
    orm_b_lerps.append(orm_b_lerp)

def ConnectBaseColorNodes():
    #Connect Texture Parameters to Lerps
    MaterialEditLibrary.connect_material_expressions(base_colors[0], '', base_color_lerps[0], 'B')
    MaterialEditLibrary.connect_material_expressions(base_colors[1], '', base_color_lerps[1], 'B')
    MaterialEditLibrary.connect_material_expressions(base_colors[2], '', base_color_lerps[2], 'B')
    MaterialEditLibrary.connect_material_expressions(base_colors[3], '', base_color_lerps[3], 'B')
    MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[4], 'B')
    MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[0], 'A')
    MaterialEditLibrary.connect_material_expressions(OneMinusNodeColor, '', base_color_lerps[0], 'Alpha')

    #Connect Vertex Color Node to base Color Lerps
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNodeColor, '')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'R', base_color_lerps[1], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'G', base_color_lerps[2], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'B', base_color_lerps[3], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', base_color_lerps[4], 'Alpha')

    # Make Lerp Connections
    MaterialEditLibrary.connect_material_expressions(base_color_lerps[0], '', base_color_lerps[1], 'A')
    MaterialEditLibrary.connect_material_expressions(base_color_lerps[1], '', base_color_lerps[2], 'A')
    MaterialEditLibrary.connect_material_expressions(base_color_lerps[2], '', base_color_lerps[3], 'A')
    MaterialEditLibrary.connect_material_expressions(base_color_lerps[3], '', base_color_lerps[4], 'A')

    # Connect last Lerp to the Base Color Channel of the Material
    MaterialEditLibrary.connect_material_property(base_color_lerps[4], '', unreal.MaterialProperty.MP_BASE_COLOR)
    return

def ConnectNormalNodes():
    # Connect Texture Parameters to Lerps
    MaterialEditLibrary.connect_material_expressions(normals[0], '', normal_lerps[0], 'B')
    MaterialEditLibrary.connect_material_expressions(normals[1], '', normal_lerps[1], 'B')
    MaterialEditLibrary.connect_material_expressions(normals[2], '', normal_lerps[2], 'B')
    MaterialEditLibrary.connect_material_expressions(normals[3], '', normal_lerps[3], 'B')
    MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[4], 'B')
    MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[0], 'A')
    MaterialEditLibrary.connect_material_expressions(OneMinusNodeNormal, '', normal_lerps[0], 'Alpha')

    # Connect Vertex Color Node to base Color Lerps
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', OneMinusNodeNormal, '')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'R', normal_lerps[1], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'G', normal_lerps[2], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'B', normal_lerps[3], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', normal_lerps[4], 'Alpha')

    # Make Lerp Connections
    MaterialEditLibrary.connect_material_expressions(normal_lerps[0], '', normal_lerps[1], 'A')
    MaterialEditLibrary.connect_material_expressions(normal_lerps[1], '', normal_lerps[2], 'A')
    MaterialEditLibrary.connect_material_expressions(normal_lerps[2], '', normal_lerps[3], 'A')
    MaterialEditLibrary.connect_material_expressions(normal_lerps[3], '', normal_lerps[4], 'A')

    # Connect last Lerp to the Base Color Channel of the Material
    MaterialEditLibrary.connect_material_property(normal_lerps[4], '', unreal.MaterialProperty.MP_NORMAL)
    return

def ConnectOcclusionNodes():
    # Connect Texture Parameters to Lerps
    MaterialEditLibrary.connect_material_expressions(orms[0], 'R', orm_r_lerps[0], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[1], 'R', orm_r_lerps[1], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[2], 'R', orm_r_lerps[2], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[3], 'R', orm_r_lerps[3], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'R', orm_r_lerps[4], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'R', orm_r_lerps[0], 'A')
    MaterialEditLibrary.connect_material_expressions(OneMinusNode_R, '', orm_r_lerps[0], 'Alpha')

    # Connect Vertex Color Node to base Color Lerps
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'A', OneMinusNode_R, '')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'R', orm_r_lerps[1], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'G', orm_r_lerps[2], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'B', orm_r_lerps[3], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'A', orm_r_lerps[4], 'Alpha')

    # Make Lerp Connections
    MaterialEditLibrary.connect_material_expressions(orm_r_lerps[0], '', orm_r_lerps[1], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_r_lerps[1], '', orm_r_lerps[2], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_r_lerps[2], '', orm_r_lerps[3], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_r_lerps[3], '', orm_r_lerps[4], 'A')

    # Connect last Lerp to the Base Color Channel of the Material
    MaterialEditLibrary.connect_material_property(orm_r_lerps[4], '', unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
    return

def ConnectRoughnessNodes():
    # Connect Texture Parameters to Lerps
    MaterialEditLibrary.connect_material_expressions(orms[0], 'G', orm_g_lerps[0], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[1], 'G', orm_g_lerps[1], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[2], 'G', orm_g_lerps[2], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[3], 'G', orm_g_lerps[3], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'G', orm_g_lerps[4], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'G', orm_g_lerps[0], 'A')
    MaterialEditLibrary.connect_material_expressions(OneMinusNode_G, '', orm_g_lerps[0], 'Alpha')

    # Connect Vertex Color Node to base Color Lerps
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'A', OneMinusNode_G, '')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'R', orm_g_lerps[1], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'G', orm_g_lerps[2], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'B', orm_g_lerps[3], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'A', orm_g_lerps[4], 'Alpha')

    # Make Lerp Connections
    MaterialEditLibrary.connect_material_expressions(orm_g_lerps[0], '', orm_g_lerps[1], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_g_lerps[1], '', orm_g_lerps[2], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_g_lerps[2], '', orm_g_lerps[3], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_g_lerps[3], '', orm_g_lerps[4], 'A')

    # Connect last Lerp to the Base Color Channel of the Material
    MaterialEditLibrary.connect_material_property(orm_g_lerps[4], '', unreal.MaterialProperty.MP_ROUGHNESS)
    return

def ConnectMetallicNodes():
    # Connect Texture Parameters to Lerps
    MaterialEditLibrary.connect_material_expressions(orms[0], 'B', orm_b_lerps[0], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[1], 'B', orm_b_lerps[1], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[2], 'B', orm_b_lerps[2], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[3], 'B', orm_b_lerps[3], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'B', orm_b_lerps[4], 'B')
    MaterialEditLibrary.connect_material_expressions(orms[4], 'B', orm_b_lerps[0], 'A')
    MaterialEditLibrary.connect_material_expressions(OneMinusNode_B, '', orm_b_lerps[0], 'Alpha')

    # Connect Vertex Color Node to base Color Lerps
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'A', OneMinusNode_B, '')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'R', orm_b_lerps[1], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'G', orm_b_lerps[2], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'B', orm_b_lerps[3], 'Alpha')
    MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'A', orm_b_lerps[4], 'Alpha')

    # Make Lerp Connections
    MaterialEditLibrary.connect_material_expressions(orm_b_lerps[0], '', orm_b_lerps[1], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_b_lerps[1], '', orm_b_lerps[2], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_b_lerps[2], '', orm_b_lerps[3], 'A')
    MaterialEditLibrary.connect_material_expressions(orm_b_lerps[3], '', orm_b_lerps[4], 'A')

    # Connect last Lerp to the Base Color Channel of the Material
    MaterialEditLibrary.connect_material_property(orm_b_lerps[4], '', unreal.MaterialProperty.MP_METALLIC)
    return

def main():
    ConnectBaseColorNodes()
    ConnectNormalNodes()
    ConnectOcclusionNodes()
    ConnectRoughnessNodes()
    ConnectMetallicNodes()
    return

# Method to run the script
main()


