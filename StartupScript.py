import unreal
import importlib
import os
import sys

sys.path.insert(1, os.path.join(unreal.SystemLibrary.get_project_directory(), os.pardir, 'PythonCode'))

import subprocess

menu_owner = "ExampleOwnerName"
tool_menus = unreal.ToolMenus.get()
owning_menu_name = "LevelEditor.LevelEditorToolBar.PlayToolBar"
python_code_directory = os.path.join(unreal.SystemLibrary.get_project_directory(), os.pardir, 'PythonCode')

import Prefixer


@unreal.uclass()
class example_SubMenuEntry(unreal.ToolMenuEntryScript):

    def init_as_toolbar_button(self):
        self.data.menu = owning_menu_name
        self.data.advanced.entry_type = unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
        self.data.icon = unreal.ScriptSlateIcon("EditorStyle", "MaterialEditor.CameraHome")
        self.data.advanced.style_name_override = "CalloutToolbar"


def Run():
    if True:  # Testing stuff
        tool_menus.unregister_owner_by_name(
            menu_owner)  # For Testing: Allow iterating on this menu python file without restarting editor

    # Create the python menu on the tool bar
    entry = example_SubMenuEntry()
    contextMenu = tool_menus.extend_menu("ContentBrowser.AssetContextMenu")
    entry.init_as_toolbar_button()
    entry.init_entry(menu_owner, owning_menu_name, "", "exampleToolbarEntry", "Python", "Python Quick Links")

    # First add an option to open the code directory
    sub_menu = tool_menus.register_menu(owning_menu_name + ".exampleToolbarEntry", "", unreal.MultiBoxType.MENU, False)
    sub_entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "OpenCodeFolder",
        "Open Code Folder",
        "Open the directory the python code is stored in",
        unreal.ToolMenuStringCommandType.PYTHON,
        "",
        "exec(open(\"" + python_code_directory + "\"+'/OpenFolders.py').read())")

    sub_menu.add_menu_entry("", sub_entry)

    # Create second entry that opens the webpage for the python API
    sub_entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "PythonAPIdocumentation",
        "Python API documentation",
        "Link to the API documenation for quick reference",
        unreal.ToolMenuStringCommandType.PYTHON,
        "",
        "unreal.SystemLibrary.launch_url(\"https://docs.unrealengine.com/5.0/en-US/PythonAPI/\")")
    sub_menu.add_menu_entry("", sub_entry)

    # Add the button to the dynamic right hand click menu on the assets for the prefixer tool
    contextMenu.add_dynamic_section("DynamicActorSection", dynamicActorSection())
    toolbar = tool_menus.extend_menu(owning_menu_name)
    toolbar.add_menu_entry_object(entry)
    tool_menus.refresh_all_widgets()


# A dynamic section for more advanced control over visibility.  You can use a normal section with add_section
@unreal.uclass()
class dynamicActorSection(unreal.ToolMenuSectionDynamic):

    @unreal.ufunction(override=True)
    def construct_sections(self, menu, context):
        menu.add_section("ExampleSectionID", "Python Tasks Section")
        AddEntries(menu, "ExampleSectionID")  # Adds options directly to the context menu


@unreal.uclass()
class example_entry_script(unreal.ToolMenuEntryScript):

    @unreal.ufunction(override=True)
    def execute(self, context):
        prefixer.runprefixer()


def AddEntries(menu, section_name):
    entry = example_entry_script()
    entry.data.icon = unreal.ScriptSlateIcon("EditorStyle", "Persona.ToggleReferencePose")
    entry.init_entry(menu_owner, "LevelEditor.AssetContextMenu", section_name, "ExampleEntryID", "Add Prefix",
                     "Example Entry Tooltip.")
    menu.add_menu_entry_object(entry)


Run()


