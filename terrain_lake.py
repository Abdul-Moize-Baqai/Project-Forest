import bpy
from mathutils import Vector
from mathutils.noise import hetero_terrain

class Terrain:
    def __init__(self, material, size=60, div=150, height=7):
        mesh = bpy.data.meshes.new("TerrainMesh")
        self.obj = bpy.data.objects.new("Terrain", mesh)
        bpy.context.collection.objects.link(self.obj)
        self.obj.data.materials.append(material.mat)

        verts, faces = [], []
        step = size / (div - 1)

        for i in range(div):
            for j in range(div):
                x = -size/2 + i*step
                y = -size/2 + j*step
                z = hetero_terrain(Vector((x/5, y/5, 0)), 1, 2.2, 8, 0) * height
                verts.append((x, y, z))

        for i in range(div-1):
            for j in range(div-1):
                a = i*div + j
                faces.append((a, a+1, a+div+1, a+div))

        mesh.from_pydata(verts, [], faces)
        mesh.update()

class Lake:
    def __init__(self, material, radius=10):
        bpy.ops.mesh.primitive_circle_add(
            vertices=128,
            radius=radius,
            location=(0, 0, 0.6)
        )
        bpy.context.active_object.scale.z = 0.15
        bpy.context.active_object.data.materials.append(material.mat)
