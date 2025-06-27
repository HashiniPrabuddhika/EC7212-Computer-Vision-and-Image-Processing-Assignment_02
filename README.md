# Image Processing Operations – EC7212 Assignment

This project is developed as part of the **EC7212 - Computer Vision and Image Processing** course. It demonstrates key image processing techniques using Python, OpenCV, and NumPy.

---

## 📌 Objectives

Python programs perform the following image processing tasks:

### ✅ Q1: Image Processing Operations
1. **Intensity Level Reduction**  
   Reduce grayscale levels from 256 to 2 in powers of 2 (e.g., 16, 4, 2).  
2. **Spatial Averaging**  
   Apply 3×3, 10×10, and 20×20 average filters to smooth images.  
3. **Image Rotation**  
   Rotate image by 45° and 90° using OpenCV rotate and affine methods.  
4. **Spatial Resolution Reduction**  
   Simulate pixelation by averaging 3×3, 5×5, and 7×7 blocks.

### ✅ Q2: Image Segmentation Techniques
1. **Otsu Thresholding with Gaussian Noise**  
   Add noise to a simple 3-class image and segment using Otsu’s method.  
2. **Region Growing Segmentation**  
   Use a seed pixel and grow region based on similarity threshold.

---

## 📁 Project Structure

```
cvip-assignment-2/
├── input/                        # Input image (grayscale)
│   └── img1.jpg
├── output/                       # Output results
│   ├── otsu_threshold.png
│   ├── otsu_display.png
│   ├── region_growing_output.png
│   └── region_growing_display.png
├── region_growing.py             # Region Growing Script (Q2)
├── otsu_threshold.py             # Otsu with Gaussian Noise (Q1)
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
