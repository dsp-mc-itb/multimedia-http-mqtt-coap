import aiocoap.resource as resource
import aiocoap
import asyncio
import base64
import cv2
import numpy as np

class VideoResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.frame_count = 0
        self.video_writer = None
        self.frame_width = 640
        self.frame_height = 480
        self.fps = 20.0

    async def render_post(self, request):
        # Decode the frame from the request payload
        frame_data = base64.b64decode(request.payload)
        frame = np.frombuffer(frame_data, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Initialize the video writer if not already done
        if self.video_writer is None:
            self.video_writer = cv2.VideoWriter('received_video.avi', 
                                                cv2.VideoWriter_fourcc(*'XVID'), 
                                                self.fps, 
                                                (self.frame_width, self.frame_height))
        
        # Write the frame to the video file
        self.video_writer.write(frame)
        self.frame_count += 1
        print(f"Frame {self.frame_count} received and saved.")

        return aiocoap.Message(code=aiocoap.CHANGED, payload=b'Frame received')

    async def shutdown(self):
        if self.video_writer:
            self.video_writer.release()

async def main():
    # Resource tree creation
    root = resource.Site()
    video_resource = VideoResource()
    root.add_resource(['video'], video_resource)

    # Create and start the server
    context = await aiocoap.Context.create_server_context(root, bind=('127.0.0.1',5683))
    print("CoAP Server running...")
    
    try:
        await asyncio.get_running_loop().create_future()  # Run forever
    finally:
        await video_resource.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
