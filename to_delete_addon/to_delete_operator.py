from typing import Set
import bpy
from bpy.types import Context

class ToDeleteOperator(bpy.types.Operator):
    bl_idname = "object.add_to_delete_collection"
    bl_label = "Add toDelete Collection"

    TO_DELETE_COLLECTION_NAME = "ToDelete"

    @classmethod
    def poll(cls, context) -> bool:
        return len(context.selected_objects) > 0

    def execute(self, context: Context) -> Set[str] | Set[int]:
        # Create a new collection called "ToDelete"
        if self.TO_DELETE_COLLECTION_NAME not in bpy.data.collections:
            bpy.ops.collection.create(name=self.TO_DELETE_COLLECTION_NAME)

        # Get the current selection
        selected_objects = bpy.context.selected_objects

        # Unlink the selected objects from the current collection
        for collection in bpy.data.collections:
            for obj in selected_objects:
                if obj.name in collection.objects:
                    collection.objects.unlink(obj)

        # Link the selected objects to the "ToDelete" collection
        for obj in selected_objects:
            if obj.name not in bpy.data.collections[self.TO_DELETE_COLLECTION_NAME].objects:
                bpy.data.collections[self.TO_DELETE_COLLECTION_NAME].objects.link(obj)

        return {'FINISHED'}
    
def draw_object_menu(self, context):
    self.layout.operator(
        ToDeleteOperator.bl_idname, text=ToDeleteOperator.bl_label
    )
    
def draw_object_context_menu(self, context):
    self.layout.separator()
    self.layout.operator(
        ToDeleteOperator.bl_idname, text=ToDeleteOperator.bl_label
    )

def register():
    bpy.types.VIEW3D_MT_object.append(draw_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_object_context_menu)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(draw_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_object_context_menu)
