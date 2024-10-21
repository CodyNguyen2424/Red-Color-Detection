import cv2
import numpy as np

class PythonDetection:
    def __init__(self):
        # Initialize the webcam
        self.cap = cv2.VideoCapture(0)

    def detect_red_objects(self):
        while True:
            # Capture each frame from the webcam
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture video frame.")
                break

            # Convert the frame to HSV (Hue, Saturation, Value) for better color filtering
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define the range of red color in HSV
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv_frame, lower_red, upper_red)

            # Second mask for detecting red colors in another hue range
            lower_red_2 = np.array([170, 120, 70])
            upper_red_2 = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv_frame, lower_red_2, upper_red_2)

            # Combine both masks to detect red
            red_mask = mask1 + mask2

            # Find contours of the red areas
            contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Draw rectangles around detected red objects
            for contour in contours:
                if cv2.contourArea(contour) > 500:  # Filter small areas
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

            # Display the frame with the rectangle(s)
            cv2.imshow("Red Object Detection", frame)

            # Press 'q' to quit the program
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of the class and start detection
    detector = PythonDetection()
    detector.detect_red_objects()
