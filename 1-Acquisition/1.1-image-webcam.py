import cv2

def capture_image():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is captured correctly
    if not ret:
        print("Error: Could not capture frame")
        return

    # Save the captured image
    cv2.imwrite("captured_image.jpg", frame)

    # Release the webcam
    cap.release()

    print("Image captured successfully!")

if __name__ == "__main__":
    capture_image()
