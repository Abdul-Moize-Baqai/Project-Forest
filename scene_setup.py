import bpy
import random
from mathutils.noise import seed_set

class SceneSetup:
    def __init__(self, frame_start=1, frame_end=250, seed=42):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        scene = bpy.context.scene
        scene.frame_start = frame_start
        scene.frame_end = frame_end

        seed_set(seed)
        random.seed(seed)

    def add_light(self):
        bpy.ops.object.light_add(
            type='SUN',
            location=(20, -30, 40)
        )

    def add_camera(self):
        bpy.ops.object.camera_add(
            location=(45, -55, 30),
            rotation=(1.1, 0, 0.8)
        )
        bpy.context.scene.camera = bpy.context.active_object
import bpy
import random
from mathutils.noise import seed_set

class SceneSetup:
    def __init__(self, frame_start=1, frame_end=250, seed=42):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        scene = bpy.context.scene
        scene.frame_start = frame_start
        scene.frame_end = frame_end

        seed_set(seed)
        random.seed(seed)

    def add_light(self):
        bpy.ops.object.light_add(type='SUN', location=(20, -30, 40))

    def add_camera(self):
        bpy.ops.object.camera_add(
            location=(45, -55, 30),
            rotation=(1.1, 0, 0.8)
        )
        bpy.context.scene.camera = bpy.context.active_object
