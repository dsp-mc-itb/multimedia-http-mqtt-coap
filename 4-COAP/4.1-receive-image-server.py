import aiocoap.resource as resource
import aiocoap
import asyncio
import base64

class ImageResource(resource.Resource):
    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        # Decode the image from the request payload
        image_data = base64.b64decode(request.payload)
        with open('received_image.jpg', 'wb') as f:
            f.write(image_data)
        print("Image received and saved.")
        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'Image received')

async def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['image'], ImageResource())

    # Create and start the server
    await aiocoap.Context.create_server_context(root, bind=('127.0.0.1',5683))
    print("CoAP Server running...")
    await asyncio.get_running_loop().create_future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
