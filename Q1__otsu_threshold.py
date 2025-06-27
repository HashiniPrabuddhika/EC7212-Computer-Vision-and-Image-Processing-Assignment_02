import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_path = "input/img1.png"
output_folder = "output"
output_path = os.path.join(output_folder, "task01_output.png")

os.makedirs(output_folder, exist_ok=True)

input_image = cv2.imread(input_path)
if input_image is None:
    raise FileNotFoundError(f"{input_path} not found!")

input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

def add_gaussian_noise(image, mean=0, std=20):
    noise = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy = image.astype(np.int16) + noise
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy

noisy_image = add_gaussian_noise(gray_image)

def otsu(image):
    histogram, _ = np.histogram(image.ravel(), bins=256, range=(0, 256))
    total_pixels = image.size
    sum_total = np.dot(np.arange(256), histogram)

    sumB = 0
    wB = 0
    max_variance = 0
    threshold = 0

    for t in range(256):
        wB += histogram[t]
        if wB == 0:
            continue
        wF = total_pixels - wB
        if wF == 0:
            break

        sumB += t * histogram[t]
        mB = sumB / wB
        mF = (sum_total - sumB) / wF

        between_variance = wB * wF * (mB - mF) ** 2

        if between_variance > max_variance:
            max_variance = between_variance
            threshold = t

    binary = (image >= threshold).astype(np.uint8) * 255
    return threshold, binary

otsu_thresh, otsu_result = otsu(noisy_image)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(input_image_rgb)
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Noisy Image (Grayscale)")
plt.imshow(noisy_image, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Otsu's Thresholding Result")
plt.imshow(otsu_result, cmap='gray')
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Histogram with Otsu Threshold")
plt.hist(noisy_image.ravel(), bins=256, range=(0, 256), color='gray')
plt.axvline(x=otsu_thresh, color='red', linestyle='--', label=f'Threshold = {otsu_thresh}')
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.show()
