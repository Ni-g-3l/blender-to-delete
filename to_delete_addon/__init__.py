bl_info = {
    "name": "ToDelete Collection",
    "author": "Nig3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "View 3D > Object Menu",
    "description": "Link Selected Items to ToDelete Collection.",
    "warning": "",
    "doc_url": "https://github.com/Nig3l/blender-to-delete",
    "category": "Object",
}

from to_delete_addon import bpy_loader

bpy_loader.init()

def register():
    bpy_loader.register()

def unregister():
    bpy_loader.unregister()

