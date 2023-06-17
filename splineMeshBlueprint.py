import unreal


def create_spline_mesh_blueprint():
    # Load original Blueprint
    unreal.log("Loading original Blueprint...")
    original_blueprint_path = "/Game/Blueprints/OriginalBlueprint"  # replace this with the path to your original Blueprint
    blueprint_path = "/Game/Blueprints/SplineMeshSpawnerBlueprint"
    original_blueprint = unreal.EditorAssetLibrary.load_asset(original_blueprint_path)

    # Duplicate the original Blueprint
    unreal.log("Creating new Blueprint by duplicating original Blueprint...")
    blueprint = unreal.EditorAssetLibrary.duplicate_asset(original_blueprint_path, blueprint_path)
    blueprint_generated_class = unreal.EditorAssetLibrary.get_blueprint_generated_class(blueprint)

    # Add a Spline Component to the Blueprint
    unreal.log("Adding Spline Component to Blueprint...")
    spline_component = blueprint_generated_class.add_component_uninitialized("SplineComponent",
                                                                             "/Script/Engine.SplineComponent")
    spline_component.set_editor_property("Mobility", unreal.ComponentMobility.STATIC)

    # Create an array of public variables to define the meshes
    meshes_to_spawn = ["Mesh1", "Mesh2", "Mesh3", "Mesh4", "Mesh5", "Mesh6", "Mesh7", "Mesh8", "Mesh9", "Mesh10",
                       "Mesh11", "Mesh12", "Mesh13", "Mesh14", "Mesh15", "Mesh16", "Mesh17", "Mesh18", "Mesh19",
                       "Mesh20"]

    # Iterate over the public variables and add them as public Static Mesh Components to the Blueprint
    for mesh_name in meshes_to_spawn:
        mesh_component = blueprint_generated_class.add_component_uninitialized("StaticMeshComponent",
                                                                               "/Script/Engine.StaticMeshComponent")
        mesh_component.set_editor_property("Mobility", unreal.ComponentMobility.STATIC)
        mesh_variable_name = "Mesh_" + mesh_name
        mesh_variable_path = "Meshes." + mesh_variable_name
        mesh_component.set_editor_property("StaticMesh",
                                           unreal.EditorAssetLibrary.get_editor_property(blueprint_generated_class,
                                                                                         mesh_variable_path))
        mesh_component.set_editor_property("CollisionEnabled", unreal.CollisionEnabledType.NO_COLLISION)
        spline_component.add_instance_component(mesh_component)

    # Save the Blueprint
    unreal.log("Saving Blueprint...")
    unreal.EditorAssetLibrary.save_loaded_asset(blueprint)

    # Log the Blueprint path
    blueprint_path = unreal.EditorAssetLibrary.get_asset_path(blueprint)
    unreal.log("Blueprint created successfully: {}".format(blueprint_path))


# Execute the function to create the Blueprint
create_spline_mesh_blueprint()
