import asyncio
from aiocoap import Context, Message, Resource

class CaptureImageResource(Resource):
    async def render_post(self, request):
        # Receive image from client
        img_bytes = request.payload

        # Save image locally (optional)
        with open('received_image.jpg', 'wb') as f:
            f.write(img_bytes)

        print("Image received from client and saved successfully!")

        return Message(payload=b"Image received successfully!")

async def main():
    # Create CoAP context
    context = await Context.create_server_context()

    # Create resource
    capture_image_resource = CaptureImageResource()

    # Add resource to context
    context.root.put_child('capture_image', capture_image_resource)

    print("CoAP server started...")

    # Run CoAP server
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
