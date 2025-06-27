import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def otsu_with_gaussian_noise():
    input_path = "input/img1.png"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read the image at {input_path}")
        return

    # Add Gaussian noise
    noise = np.random.normal(0, 10, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    # Apply Otsu's thresholding
    threshold_val, otsu_result = cv2.threshold(
        noisy_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Save thresholded result
    output_path = os.path.join(output_folder, "otsu_threshold.png")
    cv2.imwrite(output_path, otsu_result)

    # Display results
    display_path = os.path.join(output_folder, "otsu_display.png")
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Noisy Image")
    plt.imshow(noisy_img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title(f"Otsu Threshold = {threshold_val:.2f}")
    plt.imshow(otsu_result, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig(display_path)
    plt.show()

    print(f"Otsu thresholded image saved to {output_path}")
    print(f"Otsu visualization saved to {display_path}")

otsu_with_gaussian_noise()
