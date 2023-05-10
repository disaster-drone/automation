import unreal
import os
from pathlib import Path
# import sys

# sys.path.append('C:/Users/Disaster Drone/Desktop/rc_script')

# from rc_automation import upload_VR_to_gcs

def import_datatable():
    fpath = "C:/Users/paperspace/Desktop/rc_script/rc_script/OfficeScptTest.csv"
    dpath = '/Game/VRTemplate/Blueprints'

    datatable_import_task = unreal.AssetImportTask()
    datatable_import_task.filename = fpath
    datatable_import_task.destination_path = dpath
    datatable_import_task.replace_existing = True
    datatable_import_task.automated = True
    datatable_import_task.save = False

    csv_factory = unreal.CSVImportFactory()
    csv_factory.automated_import_settings.import_row_struct = unreal.load_object(None, '/Game/VRTemplate/Blueprints/CameraLocations.CameraLocations')

    datatable_import_task.factory = csv_factory
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset_tools.import_asset_tasks([datatable_import_task])


def import_images():

    IMPORT_DIR = Path(r"C:\Users\paperspace\Desktop\rc_script\rc_script\Images")
    assert IMPORT_DIR.exists()

    tasks = []

    for images in IMPORT_DIR.glob("*.jpg"):
        image_import_task = unreal.AssetImportTask()
        image_import_task.filename = str(images)
        image_import_task.destination_path = '/Game/VRTemplate/Blueprints/UI/UTA'
        image_import_task.automated = True
        tasks.append(image_import_task)

    image_asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    image_asset_tools.import_asset_tasks(tasks)

def spawn_actor():
    actor_obj = unreal.load_asset('/Game/VRTemplate/Blueprints/OfficeScptTest')
    actor_location = unreal.Vector(0.0, 0.0, 100.0)
    actor_rotation = unreal.Rotator(0.0, 0.0, -90.0)
    unreal.EditorLevelLibrary.spawn_actor_from_object(actor_obj, actor_location, actor_rotation)

asset_path = '/Game/VRTemplate/Building'
task = unreal.AssetImportTask()

f =  "C:/Users/paperspace/Desktop/rc_script/rc_script/OfficeScptTest.fbx"
task.filename = f
task.destination_path = asset_path
task.destination_name = ''
task.replace_existing = True
task.automated = True

task.options = unreal.FbxImportUI()

task.options.import_as_skeletal = False
task.options.override_full_name = True
task.options.mesh_type_to_import = unreal.FBXImportType.FBXIT_STATIC_MESH

task.options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 100.0))
task.options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, -90.0))
task.options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
task.options.static_mesh_import_data.set_editor_property('combine_meshes', True)
task.options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
task.options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
# task.options.static_mesh_import_data.set_editor_property('Coll', False)
# set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE) 


imported_asset = unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
imported_mesh = task.imported_object_paths
print(imported_mesh)

static_mesh = unreal.EditorAssetLibrary.load_asset('/Game/VRTemplate/Blueprints/OfficeScptTest.OfficeScptTest')
# Body = static_mesh.get_editor_property('body_setup')
# collision_trace_flag = unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE
# Body.set_editor_property('collision_trace_flag', collision_trace_flag)
# static_mesh.set_editor_property('body_setup', Body)

for i, name in enumerate(imported_mesh): 
    name = unreal.EditorAssetLibrary.load_asset(name)
    Body = name.get_editor_property('body_setup') 
    Body.set_editor_property('collision_trace_flag', unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE) 
    name.set_editor_property('body_setup', Body)

# import_images()
# import_datatable()
spawn_actor()
unreal.EditorAssetLibrary.save_directory('/Game', only_if_is_dirty=True, recursive=True)


# unreal.EditorAssetLibrary.sync_browser_to_objects(['/Game/VRTemplate/Blueprints/OfficeScptTest'])
unreal.EditorAssetLibrary.checkout_asset('/Game/VRTemplate/Blueprints/OfficeScptTest.OfficeScptTest')   # not working



