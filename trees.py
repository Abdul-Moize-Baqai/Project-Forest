import bpy
import random
from mathutils import Vector

# Define materials for trunk and leaves i am only making the class to handle tree creation
class Tree:
    def __init__(self, trunk_mat, leaf_mat):
        self.trunk = trunk_mat
        self.leaf = leaf_mat

    def create(self, base: Vector):
        height = random.uniform(3.5, 5.5)

        bpy.ops.mesh.primitive_cylinder_add(
            radius=random.uniform(0.15, 0.25),
            depth=1,
            location=base
        )
        trunk = bpy.context.active_object
        trunk.data.materials.append(self.trunk.mat)

        trunk.scale = (1, 1, 0.001)
        trunk.keyframe_insert("scale", frame=1)

        trunk.scale = (1, 1, height)
        trunk.location.z += height / 2
        trunk.keyframe_insert("scale", frame=120)
        trunk.keyframe_insert("location", frame=120)

        for i in range(5):
            bpy.ops.mesh.primitive_ico_sphere_add(
                radius=0.8 * (1 - i * 0.12),
                location=(base.x, base.y, base.z + height * 0.6 + i * 0.4)
            )
            bpy.context.active_object.data.materials.append(self.leaf.mat)
