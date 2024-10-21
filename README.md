# Red Object Detection using OpenCV

This project detects red-colored objects in a real-time video feed using a webcam. It utilizes OpenCV to capture video frames, convert them to HSV color space, and identify objects within a specified red color range. Detected objects are highlighted with rectangles in the live video feed.

## Features

- Real-time detection of red objects using the webcam.
- Highlights detected red objects with bounding rectangles.
- Adjustable HSV range for detecting different shades of red.
- Easy-to-use interface: press 'q' to quit the program.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library
- Numpy library

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/red-object-detection.git
   cd red-object-detection
   ```

2. **Install the required libraries:**

   You can use `pip` to install the dependencies.

   ```bash
   pip install opencv-python numpy
   ```

## Usage

1. **Run the script:**

   Simply run the `red_object_detection.py` file.

   ```bash
   python red_object_detection.py
   ```

2. **Controls:**

   - The webcam feed will open automatically.
   - The red objects in the frame will be outlined by rectangles.
   - Press **'q'** to exit the video feed.

## How it Works

- The script uses the HSV (Hue, Saturation, Value) color space for better color segmentation.
- It defines two HSV color ranges to detect red objects:
  - One range for detecting lighter red shades.
  - Another range for darker red shades.
- The detected red areas are outlined with bounding rectangles in the live video feed.

## Customization

- You can modify the HSV color ranges to detect different colors or adjust the sensitivity.
- Adjust the minimum contour area (`500` in this example) to detect larger or smaller red objects.
  
  ```python
  if cv2.contourArea(contour) > 500:  # Minimum size filter
  ```

## License

This project is licensed under the MIT License.

---

Feel free to modify or add more sections based on your project's details!
