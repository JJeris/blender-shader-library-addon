bl_info = {
    "name": "Shader Library",
    "author": "JJeris",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "View3D > ToolShelf",
    "description": "Adds a new Shader tp yout object",
    "warning": "",
    "doc_url": "",
    "category": "Add Shader",
}

import bpy

class ShaderMainPanel (bpy.types.Panel):
    """Creates a Panel in the tool shelf"""
    bl_label = "Shader Library" ## Name on the panel
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Library"    
   
   
    def draw(self):
        layout = self.layout
    
def register():
    bpy.utils.register_class(ShaderMainPanel)
def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
if __name__ == "__main__":
    register()
    
# class HelloWorldPanel(bpy.types.Panel):
#     """Creates a Panel in the Object properties window"""
#     bl_label = "Hello World Panel"
#     bl_idname = "OBJECT_PT_hello"
#     bl_space_type = 'PROPERTIES'
#     bl_region_type = 'WINDOW'
#     bl_context = "object"

#     def draw(self, context):
#         layout = self.layout

#         obj = context.object

#         row = layout.row()
#         row.label(text="Hello world!", icon='WORLD_DATA')

#         row = layout.row()
#         row.label(text="Active object is: " + obj.name)
#         row = layout.row()
#         row.prop(obj, "name")

#         row = layout.row()
#         row.operator("mesh.primitive_cube_add")


# def register():
#     bpy.utils.register_class(HelloWorldPanel)


# def unregister():
#     bpy.utils.unregister_class(HelloWorldPanel)


# if __name__ == "__main__":
#     register()