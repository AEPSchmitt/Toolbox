from PIL import Image

# Generates a series of frames for an animation of a growing circle
# Used to create animation sprites for my game: https://aepschmitt.itch.io/night-chime

WIDTH, HEIGHT = 75, 75
CENTER = (WIDTH // 2, HEIGHT // 2)
max_radius = max(CENTER[0], CENTER[1])
stroke_thickness = 1
total_frames = max_radius + 1  # from radius 0 to max_radius inclusive

def is_in_ring(x, y, cx, cy, radius, thickness):
    dx = x - cx
    dy = y - cy
    dist_sq = dx*dx + dy*dy
    return (radius - thickness) ** 2 <= dist_sq <= (radius + thickness) ** 2

for frame in range(total_frames):
    img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))  # transparent bg
    pixels = img.load()

    radius = frame
    alpha = int(255 * (1 - frame / (total_frames - 1)))

    if radius == 0:
        # Only center pixel for radius 0
        pixels[CENTER[0], CENTER[1]] = (255, 255, 255, alpha)
    else:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if is_in_ring(x, y, CENTER[0], CENTER[1], radius, stroke_thickness):
                    pixels[x, y] = (255, 255, 255, alpha)

    img.save(f'circle_{frame:03}.png')
