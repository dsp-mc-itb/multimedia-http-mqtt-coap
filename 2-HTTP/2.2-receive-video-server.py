from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Receive video from client
    file = request.files['video']
    file.save('received_video.avi')

    print("Video received from client and saved successfully!")

    return "Video received successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
