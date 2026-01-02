from scene_setup import SceneSetup
from materials import create_materials
from terrain_lake import Terrain, Lake
from trees import Tree
from weather_forest import Forest, Rain

def main():
    # Scene
    scene = SceneSetup()
    scene.add_light()
    scene.add_camera()

    # Materials
    materials = create_materials()

    # Environment
    terrain = Terrain(materials["mud"])
    lake = Lake(materials["lake"])

    # Vegetation
    tree = Tree(materials["trunk"], materials["leaf"])
    forest = Forest(tree)
    forest.populate(count=10)

    # Weather
    rain = Rain()

    print("Scene generation complete")


if __name__ == "__main__":
    main()
