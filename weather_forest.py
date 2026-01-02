import bpy
import math
import random
from mathutils import Vector
from mathutils.noise import hetero_terrain

class Forest:
    def __init__(self, tree):
        self.tree = tree

    def populate(self, count=10):
        for i in range(count):
            angle = i * (math.tau / count)
            d = random.uniform(22, 30)
            x, y = math.cos(angle)*d, math.sin(angle)*d
            z = hetero_terrain(Vector((x/5, y/5, 0)), 1, 2.2, 8, 0) * 7 + 0.5
            self.tree.create(Vector((x, y, z)))

class Rain:
    def __init__(self):
        bpy.ops.mesh.primitive_plane_add(size=80, location=(0, 0, 25))
        emitter = bpy.context.active_object
        ps = emitter.modifiers.new("Rain", 'PARTICLE_SYSTEM')
        s = ps.particle_system.settings
        s.count = 12000
        s.lifetime = 50
        s.render_type = 'HALO'
        s.particle_size = 0.02
