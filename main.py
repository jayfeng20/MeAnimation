from ursina import *

app = Ursina()

# Add a directional light
DirectionalLight(parent=scene, y=2, z=-3, shadows=True)

# Add ambient light to brighten shadowed areas
AmbientLight(color=color.rgba(255, 255, 255, 0.3))

# Create the player character
player = Entity(
    model="objects/chr_knight.vox.obj",
    texture="objects/chr_knight.png",
    color=color.orange,
    scale=(0.5, 0.5, 0.5),
    position=(0, 0.25, 0),
)


# Update function to control player movement
def update():
    player.rotation_y += 0.3
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


camera.orthographic = False
camera.position = (0, 2, -5)  # Adjust for a better perspective
camera.look_at(player)

# Run the Ursina application
app.run()
