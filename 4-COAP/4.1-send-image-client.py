import cv2
import aiocoap
import asyncio
import base64

async def send_image():
    # Capture image from webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture image")
        return

    # Encode the image to JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    image_data = base64.b64encode(buffer.tobytes())

    # Create CoAP client context
    context = await aiocoap.Context.create_client_context()

    # Create CoAP POST request
    request = aiocoap.Message(code=aiocoap.POST, uri='coap://127.0.0.1/image', payload=image_data)

    # Send the request and await response
    response = await context.request(request).response

    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.run(send_image())
