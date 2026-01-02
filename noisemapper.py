import numpy as np
from PIL import Image

# Generates a 'heightmap.png' file with a given resolution, intensity and noise type

WIDTH = 512
HEIGHT = 512
NOISE_INTENSITY = 1.0   # 0.1 = very smooth, 2.0 = very rough
NOISE_TYPE = "voronoi"  # "value", "perlin", "voronoi"
OUTPUT_FILE = "heightmap.png"

# Helper function(s)

def normalize(data):
    data = data - data.min()
    return (data / data.max() * 255).astype(np.uint8)


# Smoothed random value noise

def value_noise(width, height, smoothness=8):
    noise = np.random.rand(height, width)

    for _ in range(smoothness):
        noise = (
            noise +
            np.roll(noise, 1, 0) +
            np.roll(noise, -1, 0) +
            np.roll(noise, 1, 1) +
            np.roll(noise, -1, 1)
        ) / 5

    return noise


# Perlin(like) noise

def lerp(a, b, t):
    return a + t * (b - a)


def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3


def perlin_noise(width, height, scale=50):
    gx = width // scale + 2
    gy = height // scale + 2

    gradients = np.random.rand(gy, gx, 2) * 2 - 1

    noise = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            xf = x / scale
            yf = y / scale

            x0 = int(xf)
            y0 = int(yf)

            dx = xf - x0
            dy = yf - y0

            g00 = gradients[y0, x0]
            g10 = gradients[y0, x0 + 1]
            g01 = gradients[y0 + 1, x0]
            g11 = gradients[y0 + 1, x0 + 1]

            d00 = g00 @ np.array([dx, dy])
            d10 = g10 @ np.array([dx - 1, dy])
            d01 = g01 @ np.array([dx, dy - 1])
            d11 = g11 @ np.array([dx - 1, dy - 1])

            u = fade(dx)
            v = fade(dy)

            nx0 = lerp(d00, d10, u)
            nx1 = lerp(d01, d11, u)
            value = lerp(nx0, nx1, v)

            noise[y, x] = value

    return noise

# Voronoi noise

def voronoi_noise(width, height, points=40):
    seeds = np.random.rand(points, 2)
    seeds[:, 0] *= width
    seeds[:, 1] *= height

    noise = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            distances = np.sqrt((seeds[:, 0] - x)**2 + (seeds[:, 1] - y)**2)
            noise[y, x] = np.min(distances)

    return noise


if NOISE_TYPE == "value":
    data = value_noise(WIDTH, HEIGHT, int(10 / NOISE_INTENSITY))

elif NOISE_TYPE == "perlin":
    data = perlin_noise(WIDTH, HEIGHT, scale=int(60 / NOISE_INTENSITY))

elif NOISE_TYPE == "voronoi":
    data = voronoi_noise(WIDTH, HEIGHT, points=int(50 * NOISE_INTENSITY))

else:
    raise ValueError("Invalid NOISE_TYPE")

# Normalize and save
heightmap = normalize(data)
image = Image.fromarray(heightmap, mode="L")
image.save(OUTPUT_FILE)

print(f"Heightmap saved as {OUTPUT_FILE} using '{NOISE_TYPE}' noise.")
