import numpy as np
from PIL import Image

WIDTH = 512
HEIGHT = 512
NOISE_INTENSITY = 1.0  # 0.1 = very smooth, 2.0 = very rough
OUTPUT_FILE = "heightmap.png"

def smooth_noise(data, passes=4):
    for _ in range(passes):
        data = (
            np.roll(data, 1, axis=0) +
            np.roll(data, -1, axis=0) +
            np.roll(data, 1, axis=1) +
            np.roll(data, -1, axis=1) +
            data
        ) / 5
    return data

# Base noise
noise = np.random.rand(HEIGHT, WIDTH)

# Smoothe
smoothed = smooth_noise(noise, passes=int(10 / NOISE_INTENSITY))

# Normalize to 0–255
heightmap = (smoothed - smoothed.min()) / (smoothed.max() - smoothed.min())
heightmap = (heightmap * 255).astype(np.uint8)

# Save image
image = Image.fromarray(heightmap, mode="L")
image.save(OUTPUT_FILE)

print(f"Heightmap saved as '{OUTPUT_FILE}'")
