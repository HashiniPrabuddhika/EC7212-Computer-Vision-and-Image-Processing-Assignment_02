# Image Segmentation Techniques in Python – EC7212 Assignment

This repository contains implementations of two fundamental image segmentation techniques in Python using OpenCV and NumPy.

---

## Objectives

Python programs perform the following image processing tasks:

### Image Segmentation Techniques
1. **Otsu Thresholding with Gaussian Noise**  
   Add noise to a simple 3-class image and segment using Otsu’s method. 
   This technique enhances a synthetic grayscale image with Gaussian noise to simulate real-world imperfections. Otsu's algorithm is then applied to automatically determine the optimal threshold for separating foreground and background. The result demonstrates robust binarization even in noisy conditions. 
2. **Region Growing Segmentation**  
   Starting from a user-defined seed pixel, this method recursively expands the segmented region by evaluating pixel intensity similarity within a predefined threshold. It effectively segments objects based on local homogeneity, making it suitable for separating regions with subtle variations. The implementation is efficient and well-suited for grayscale object-based segmentation tasks.


---

## 📁 Project Structure

```
EC7212-Computer-Vision-and-Image-Processing-Assignment_02/
├── input/                        # Input image
│   └── img1.png
├── output/                       # Output results
│   ├── otsu_threshold.png
│   ├── otsu_display.png
│   ├── region_growing_output.png
│   └── region_growing_display.png
├── Q1__otsu_threshold.py         # Otsu with Gaussian Noise (Q1)
├── Q2__region_growing.py         # Region Growing Script (Q2)
├── README.md                     # Project documentation
└── requirements.txt              # Dependencies
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.7+
- OpenCV
- NumPy
- Matplotlib

### Setup Instructions

```bash
# Clone repo (if hosted online)
git clone https://github.com/your-username/EC7212-Assignment.git
cd EC7212-Assignment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### Run Scripts

```bash
python otsu_threshold.py       # For Q2 - Otsu Threshold
python region_growing.py       # For Q2 - Region Growing
```

---

## 📷 Results and Explanations

### 🧪 Otsu Thresholding
- Gaussian noise is added to a synthetic image.
- Otsu’s method automatically selects the best threshold.
- Output: `otsu_threshold.png`, `otsu_display.png`

### 🌱 Region Growing
- Starts from a seed point and grows based on intensity similarity.
- Output: `region_growing_output.png`, `region_growing_display.png`

---

## 📂 Output Preview

| Task                    | Output File                   |
|-------------------------|-------------------------------|
| Otsu Thresholding       | `otsu_threshold.png`          |
| Otsu Visualization      | `otsu_display.png`            |
| Region Growing Output   | `region_growing_output.png`   |
| Region Growing Display  | `region_growing_display.png`  |

---
