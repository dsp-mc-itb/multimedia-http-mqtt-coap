import cv2
import aiocoap
import asyncio
import base64

async def send_frame(context, frame):
    # Encode the frame to JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    frame_data = base64.b64encode(buffer.tobytes())

    # Create CoAP POST request
    request = aiocoap.Message(code=aiocoap.POST, uri='coap://127.0.0.1/video', payload=frame_data)

    # Send the request and await response
    response = await context.request(request).response
    print('Result: %s\n%r' % (response.code, response.payload))

async def send_video():
    # Capture video from webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 20)

    if not cap.isOpened():
        print("Failed to open webcam")
        return

    # Create CoAP client context
    context = await aiocoap.Context.create_client_context()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            await send_frame(context, frame)
            await asyncio.sleep(0.05)  # Send frames at approximately 20 FPS
    finally:
        cap.release()

if __name__ == "__main__":
    asyncio.run(send_video())
