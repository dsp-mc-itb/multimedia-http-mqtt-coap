import cv2

def display_video():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is captured correctly
        if not ret:
            print("Error: Could not capture frame")
            break

        # Display the frame
        cv2.imshow('frame', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_video()
