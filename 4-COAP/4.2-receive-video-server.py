import asyncio
from aiocoap import Context, Message, Resource

class CaptureVideoResource(Resource):
    async def render_post(self, request):
        # Receive video from client
        video_data = request.payload

        # Save video locally (optional)
        with open('received_video.avi', 'wb') as f:
            f.write(video_data)

        print("Video received from client and saved successfully!")

        return Message(payload=b"Video received successfully!")

async def main():
    # Create CoAP context
    context = await Context.create_server_context()

    # Create resource
    capture_video_resource = CaptureVideoResource()

    # Add resource to context
    context.root.put_child('capture_video', capture_video_resource)

    print("CoAP server started...")

    # Run CoAP server
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
