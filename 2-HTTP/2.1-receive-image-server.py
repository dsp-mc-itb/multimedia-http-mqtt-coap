from flask import Flask, request
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Receive image from client
    file = request.files['image']
    nparr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Save image locally (optional)
    cv2.imwrite('received_image.jpg', img)

    print("Image received from client and saved successfully!")

    return "Image received successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
