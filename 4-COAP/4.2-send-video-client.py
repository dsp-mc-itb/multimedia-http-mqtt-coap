import cv2
import asyncio
from aiocoap import Context, Message, POST

def capture_video():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640, 480))

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is captured correctly
        if ret:
            # Display the frame
            cv2.imshow('frame', frame)

            # Write the frame into the video file
            out.write(frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("Video captured successfully!")

async def send_video():
    # Read video file
    with open("captured_video.avi", "rb") as f:
        video_data = f.read()

    # Create CoAP context
    context = await Context.create_client_context()

    # Create CoAP message
    request = Message(code=POST, payload=video_data)
    request.opt.uri_host = '34.135.8.134'  # Replace with server IP
    request.opt.uri_path = ('capture_video',)

    # Send CoAP message
    response = await context.request(request).response

    print("Video sent to server successfully!")

if __name__ == "__main__":
    capture_video()
    asyncio.run(send_video())
