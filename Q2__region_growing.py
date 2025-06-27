import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def region_growing(img, seed, threshold=10):
    h, w = img.shape
    visited = np.zeros((h, w), dtype=bool)
    region = np.zeros((h, w), dtype=np.uint8)

    seed_val = img[seed]
    stack = [seed]

    while stack:
        y, x = stack.pop()
        if visited[y, x]:
            continue
        visited[y, x] = True

        if abs(int(img[y, x]) - int(seed_val)) <= threshold:
            region[y, x] = 255
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < h) and (0 <= nx < w) and not visited[ny, nx]:
                        stack.append((ny, nx))
    return region

def run_region_growing():
    input_path = "input/img1.png"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not read the image.")
        return

    seed = (30, 30)  
    region = region_growing(img, seed, threshold=10)

    output_path = os.path.join(output_folder, "region_growing_output.png")
    display_path = os.path.join(output_folder, "region_growing_display.png")

    cv2.imwrite(output_path, region)

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title("Input Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Region Grown Output")
    plt.imshow(region, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(display_path)
    plt.show()

    print(f"Region grown image saved to {output_path}")
    print(f"Visualization saved to {display_path}")

run_region_growing()
