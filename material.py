import bpy

class Material:
    def __init__(self, name, color, roughness):
        self.mat = bpy.data.materials.new(name)
        self.mat.use_nodes = True
        bsdf = self.mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        self.mat.diffuse_color = color

def create_materials():
    return {
        "mud": Material("Mud_Mat", (0.25, 0.18, 0.10, 1), 0.9),
        "lake": Material("Lake_Mat", (0.05, 0.25, 0.60, 1), 0.1),
        "trunk": Material("Trunk_Mat", (0.35, 0.20, 0.10, 1), 0.8),
        "leaf": Material("Leaf_Mat", (0.10, 0.70, 0.25, 1), 0.6),
    }
