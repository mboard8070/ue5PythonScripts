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
VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), 0, -300)
VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), 0, -400)

# Create a Vertex Color node for each ORM channel
VertexColorNode_ORM_R = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), 0, -150)
VertexColorNode_ORM_G = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), 0, 0)
VertexColorNode_ORM_B = MaterialEditLibrary.create_material_expression(MeshMaterial, unreal.MaterialExpressionVertexColor.static_class(), 0, 150)

# Create a 1-x nodes for each channel so that the texures from 5 to 1 can loop
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
    NormalParam.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    OrmParam.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))

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

# Connect texture parameters to lerp nodes
for i in range(5):
    MaterialEditLibrary.connect_material_expressions(base_colors[i], '', base_color_lerps[i], 'B')
    #MaterialEditLibrary.connect_material_expressions(base_colors[i + 1], '', base_color_lerps[i], 'B')


    MaterialEditLibrary.connect_material_expressions(normals[i], '', normal_lerps[i], 'A')
    MaterialEditLibrary.connect_material_expressions(normals[i + 1], '', normal_lerps[i], 'B')

    # ORM connections
    MaterialEditLibrary.connect_material_expressions(orms[i], 'R', orm_r_lerps[i], 'A')
    MaterialEditLibrary.connect_material_expressions(orms[i + 1], 'R', orm_r_lerps[i], 'B')

    MaterialEditLibrary.connect_material_expressions(orms[i], 'G', orm_g_lerps[i], 'A')
    MaterialEditLibrary.connect_material_expressions(orms[i + 1], 'G', orm_g_lerps[i], 'B')

    MaterialEditLibrary.connect_material_expressions(orms[i], 'B', orm_b_lerps[i], 'A')
    MaterialEditLibrary.connect_material_expressions(orms[i + 1], 'B', orm_b_lerps[i], 'B')

    if i > 0:
        MaterialEditLibrary.connect_material_expressions(base_color_lerps[i - 1], '', base_color_lerps[i], 'Alpha')
        MaterialEditLibrary.connect_material_expressions(normal_lerps[i - 1], '', normal_lerps[i], 'Alpha')
        MaterialEditLibrary.connect_material_expressions(orm_r_lerps[i - 1], '', orm_r_lerps[i], 'Alpha')
        MaterialEditLibrary.connect_material_expressions(orm_g_lerps[i - 1], '', orm_g_lerps[i], 'Alpha')
        MaterialEditLibrary.connect_material_expressions(orm_b_lerps[i - 1], '', orm_b_lerps[i], 'Alpha')

#Special Connections for Base Color
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNodeColor, '', base_color_lerps[0], 'Alpha')

    # Connect the Vertex Color node to the alpha input of base color and normal lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNodeColor, '')


# Connect the individual Vertex Color nodes to the alpha input of ORM lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_R, 'R', orm_r_lerps[i], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_G, 'G', orm_g_lerps[i], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_ORM_B, 'B', orm_b_lerps[i], 'Alpha')


#Connect Result of each network to its channel
MaterialEditLibrary.connect_material_property(base_color_lerps[-1], "", unreal.MaterialProperty.MP_BASE_COLOR)
MaterialEditLibrary.connect_material_property(normal_lerps[-1], "", unreal.MaterialProperty.MP_NORMAL)
MaterialEditLibrary.connect_material_property(orm_r_lerps[-1], "", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(orm_g_lerps[-1], "", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(orm_b_lerps[-1], "", unreal.MaterialProperty.MP_METALLIC)