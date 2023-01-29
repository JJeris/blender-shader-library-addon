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
   
   
    def draw(self, context): ## Draw needs both self and context, 2 args
        """Draws the panel for the Shader Library addon"""
        layout = self.layout
        row = layout.row()
        
        row.label(text = "Select a Shader to be added.")
        row.operator("")
        
        
        
class SHADER_OT_DIAMOND(bpy.types.Operator):
    """Create a Custom Operator for the Diamond Shader"""
    bl_label = "Diamond" 
    bl_idname = "shader.diamond.operator"
    
    def execute(self, context):
        """Creates a new shader called Diamond"""
        
        ###SET UP
        
        ## Creating a New Shader and calling it Diamond
        material_diamond = bpy.data.materials.new(name = "Diamond")
        ## Enabling Use Nodes
        material_diamond.use_node = True
        
        ## Removes the automatically loaded "Principled BSDF" node
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get("Principled BSDF"))
        
        ## Create a reference to the Material Output
        material_output = material_diamond.node_tree.nodes.get("Material Output")
        ## Set location of node
        material_output.location = (-400, 0) ##(x,y) coordinates
    
        ### GLASS NODES
        
        ## Adding Glass1 Node
        glass1_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeBsdfGlass")
        ## Set location of node
        glass1_node.location = (-600, 0)
        ## Setting the Default Color
        glass1_node.inputs[0].default_value = (1, 0, 0, 1) ## RGBA. Red
        ## Setting the Default IOR Value
        glass1_node.inputs[2].default_value = 1.446 ## IOR - Index of refraction
        
        ## Adding Glass2 Node
        glass2_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeBsdfGlass")
        ## Set location of node
        glass2_node.location = (-600,-150)
        ## Setting the Default Color
        glass2_node.inputs[0].default_value = (0, 1, 0, 1) ## RGBA. Red
        ## Setting the Default IOR Value
        glass2_node.inputs[2].default_value = 1.450 ## IOR - Index of refraction

        ## Adding Glass3 Node
        glass3_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeBsdfGlass")
        ## Set location of node
        glass3_node.location = (-600,-300)
        ## Setting the Default Color
        glass3_node.inputs[0].default_value = (0, 0, 1, 1) ## RGBA. Red
        ## Setting the Default IOR Value
        glass3_node.inputs[2].default_value = 1.500 ## IOR - Index of refraction
        
        
        
        ### ADD NODES
        
        ## Create the Add Shader Node and Reference it as "Add1"
        add1_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeAddShader")
        add1_node.location = (-400,-50)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False

        ## Create the Add Shader Node and Reference it as "Add2"
        add2_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeAddShader")
        add2_node.location = (-100,0)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False


        ### GLASS4
        ## Creating the Glass Node and Reference it as "glass4"
        glass4_node = material_diamond.node_tree.nodes.new(type = "ShaderNodeBsdfGlass")
        ## Set location of node
        glass4_node.location = (-150,-150)
        ## Setting the Default Color
        glass3_node.inputs[0].default_value = (1, 1, 1, 1) ## RGBA. Red
        ## Setting the Default IOR Value
        glass3_node.inputs[2].default_value = 1.450 ## IOR - Index of refraction
        ## Deselect the node
        glass4_node.select = False
        
        
        
        ### MIX
        
        ## Create the Mix Shader Node and Reference it as "Mix1"
        mix1_node = material_diamond_diamond.node_tree.nodes.new("ShaderNodeMixShader")
        ## Set location of node
        mix1_node.location = (200,0)
        ## Deselect the Node
        mix1_node.select - False
        
        
        ### Linking
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])

        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])

        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    
def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)

if __name__ == "__main__":
    register()
