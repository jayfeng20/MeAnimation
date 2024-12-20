from ursina import *

# Initialize the Ursina application
app = Ursina()
window.render_mode = "high"
# Create the ground
ground = Entity(
    model="plane",
    texture="white_cube",
    color=color.azure,
    scale=(10, 1, 10),
    position=(0, 0, 0),
)

# Create the player character
player = Entity(
    model="cube", color=color.orange, scale=(0.5, 0.5, 0.5), position=(0, 0.25, 0)
)


# Update function to control player movement
def update():
    # Move player based on key input
    if held_keys["w"]:  # Move forward
        player.position += Vec3(0, 0, 0.1)
    if held_keys["s"]:  # Move backward
        player.position += Vec3(0, 0, -0.1)
    if held_keys["a"]:  # Move left
        player.position += Vec3(-0.1, 0, 0)
    if held_keys["d"]:  # Move right
        player.position += Vec3(0.1, 0, 0)

    # Keep player within the ground boundary
    player.x = max(-4.5, min(4.5, player.x))
    player.z = max(-4.5, min(4.5, player.z))


# Add a camera
camera.position = (0, 10, -15)
camera.rotation_x = 30


# 7. Use Higher-Quality Models
# Ensure that your models (e.g., from MagicaVoxel) have sufficient detail for better visuals. Export them at a higher resolution and import them into your Ursina project.
# Entity(model='my_voxel_model.obj', texture='texture.png')


# Run the Ursina application
app.run()
