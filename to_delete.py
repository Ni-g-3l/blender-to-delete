import bpy

bl_info = {
    "name": "ToDelete Collection",
    "author": "Nig3l",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "location": "View 3D > Object Menu",
    "description": "Link selected objects to ToDelete Collection",
    "warning": "",
    "doc_url": "https://github.com/Ni-g-3l/blender-to-delete",
    "category": "Object",
}


class ToDeleteOperator(bpy.types.Operator):
    bl_idname = "object.add_to_delete_collection"
    bl_label = "Add toDelete Collection"
    
    TO_DELETE_COLLECTION_NAME = "ToDelete"
    
    def execute(self, context):
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
    bpy.utils.register_class(ToDeleteOperator)
    bpy.types.VIEW3D_MT_object.append(draw_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_object_context_menu)

def unregister():
    bpy.utils.unregister_class(ToDeleteOperator)
    bpy.types.VIEW3D_MT_object.remove(draw_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_object_context_menu)

if __name__ == "__main__":
    register()

