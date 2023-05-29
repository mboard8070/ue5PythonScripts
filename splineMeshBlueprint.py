import unreal


def create_spline_mesh_blueprint():
    # Initialize the Unreal Engine Python API
    unreal.log("Initializing Unreal Engine Python API...")
    unreal.log_opened()
    unreal.SystemLibrary.initialize_python_if_needed()

    # Create a new Blueprint
    unreal.log("Creating new Blueprint...")
    blueprint = unreal.EditorAssetLibrary.new_blueprint_generated_class(parent_class=None, outer_package_path="/Game/Blueprints", name="SplineMeshSpawnerBlueprint")
    blueprint_generated_class = unreal.EditorAssetLibrary.try_get_asset_blueprint_class(blueprint)
    blueprint_generated_class.set_metadata_tag("BlueprintType", "BPTYPE_Normal")
    blueprint_generated_class.set_metadata_tag("HideCategories", "Utilities")

    # Add a Spline Component to the Blueprint
    unreal.log("Adding Spline Component to Blueprint...")
    spline_component = blueprint_generated_class.add_component_uninitialized("SplineComponent", "/Script/Engine.SplineComponent")
    spline_component.set_editor_property("Mobility", unreal.ComponentMobility.STATIC)

    # Add a Spline Mesh Component to the Blueprint
    unreal.log("Adding Spline Mesh Component to Blueprint...")
    spline_mesh_component = blueprint_generated_class.add_component_uninitialized("SplineMeshComponent", "/Script/Engine.SplineMeshComponent")
    spline_mesh_component.set_editor_property("Mobility", unreal.ComponentMobility.STATIC)

    # Set the Spline Mesh Component properties
    spline_mesh_component.set_editor_property("ForwardAxis", unreal.ESplineMeshAxis.Z)
    spline_mesh_component.set_editor_property("CollisionEnabled", unreal.SplineMeshCollisionEnabledType.NO_COLLISION)

    # Create an array of meshes to spawn along the spline
    meshes_to_spawn = ["/Game/Meshes/Mesh1", "/Game/Meshes/Mesh2", "/Game/Meshes/Mesh3",
                       "/Game/Meshes/Mesh4", "/Game/Meshes/Mesh5", "/Game/Meshes/Mesh6",
                       "/Game/Meshes/Mesh7", "/Game/Meshes/Mesh8", "/Game/Meshes/Mesh9",
                       "/Game/Meshes/Mesh10", "/Game/Meshes/Mesh11", "/Game/Meshes/Mesh12",
                       "/Game/Meshes/Mesh13", "/Game/Meshes/Mesh14", "/Game/Meshes/Mesh15",
                       "/Game/Meshes/Mesh16", "/Game/Meshes/Mesh17", "/Game/Meshes/Mesh18",
                       "/Game/Meshes/Mesh19", "/Game/Meshes/Mesh20"]

    # Iterate over the meshes and add them to the Spline Mesh Component
    for mesh_path in meshes_to_spawn:
        spline_mesh_component.add_spline_mesh_point(mesh_path)

    # Save the Blueprint
    unreal.log("Saving Blueprint...")
    unreal.EditorAssetLibrary.save_loaded_asset(blueprint)

    # Log the Blueprint path
    blueprint_path = unreal.EditorAssetLibrary.get_asset_path(blueprint)
    unreal.log("Blueprint created successfully: {}".format(blueprint_path))


# Execute the function to create the Blueprint
create_spline_mesh_blueprint()
