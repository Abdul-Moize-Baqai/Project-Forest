
---

## How the Project Works
- `main.py` acts as the **controller**. It does not contain logic for geometry or effects.
- Each feature is implemented in its own module.
- When `main.py` is run inside Blender, it imports and executes all modules to generate the complete scene.

This modular approach follows standard software engineering practices and avoids tightly coupled code.

---

## Team Contributions
Each team member is responsible for **one independent module**, committed separately to the repository.

| Team Member | File | Responsibility |
|------------|------|----------------|
| Abdul Moize Baqai | `scene_setup.py` | Scene initialization, lighting, camera |
| Sarman Tipu | `materials.py` | Material creation and management |
| Soban Mujtaba | `terrain_lake.py` | Procedural terrain and lake |
| Bilal Tariq | `trees.py` | Tree generation and growth animation |
| Qasim Mustaq | `weather_forest.py` | Forest distribution and rain particles |

This ensures:
- Clear ownership
- Transparent contribution history
- Easy evaluation using Git commit logs

---

## How to Run the Project
1. Open **Blender**
2. Go to the **Scripting** workspace
3. Open `main.py`
4. Ensure all files are in the same folder
5. Click **Run Script**

The scene will automatically:
- Reset the workspace
- Generate terrain and lake
- Populate trees
- Add rain and camera

---

## Tools & Technologies
- **Blender**
- **Python (bpy API)**
- **Procedural noise (hetero_terrain)**
- **Particle systems**
- **Git for version control**

---

## Design Philosophy
- Modular code over monolithic scripts
- One feature per file
- Single orchestration point (`main.py`)
- Reproducible results using seeded randomness

This structure reflects real-world procedural graphics and software development workflows.

---

## Notes
- `main.py` is written once and not modified by individual contributors.
- All functionality is added via separate modules to ensure fair contribution tracking.
