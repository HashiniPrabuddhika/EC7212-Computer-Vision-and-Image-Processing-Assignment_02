import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_path = "input/img2.jpg"
output_folder = "output"
output_filename = "region_growing_output.png"
output_path = os.path.join(output_folder, output_filename)

os.makedirs(output_folder, exist_ok=True)

image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"{input_path} not found!")

def region_growing(image, seeds, threshold=10):
    height, width = image.shape
    segmented = np.zeros_like(image, dtype=np.uint8)
    visited = np.zeros_like(image, dtype=bool)

    queue = list(seeds)
    seed_values = [image[y, x] for x, y in seeds]
    mean_value = np.mean(seed_values)

    while queue:
        x, y = queue.pop(0)
        if visited[y, x]:
            continue
        visited[y, x] = True

        current_value = image[y, x]
        if abs(int(current_value) - int(mean_value)) <= threshold:
            segmented[y, x] = 255

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < width) and (0 <= ny < height) and not visited[ny, nx]:
                        queue.append((nx, ny))

    return segmented

seed_points = [(100, 150), (120, 170), (180, 170), (190, 150)]  

segmented_mask = region_growing(image, seed_points, threshold=10)

image_marked = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for x, y in seed_points:
    cv2.circle(image_marked, (x, y), radius=4, color=(255, 0, 0), thickness=-1)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image with Seeds")
plt.imshow(cv2.cvtColor(image_marked, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Region Growing Segmentation")
plt.imshow(segmented_mask, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.show()
