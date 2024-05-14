import cv2
import requests

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

    # Release the webcam
    cap.release()

    # Encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', frame)

    # Send image to server
    url = 'http://34.133.55.11/upload'
    files = {'image': img_encoded.tobytes()}
    response = requests.post(url, files=files)

    print("Image sent to server successfully!")

if __name__ == "__main__":
    capture_image()
