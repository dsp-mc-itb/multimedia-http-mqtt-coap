import cv2
import paho.mqtt.client as mqtt
import time

# MQTT Broker details
broker_address = "34.133.55.11"
broker_port = 1883
topic = "webcam"

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Connect to MQTT broker
client = mqtt.Client("webcam_publisher")
client.connect(broker_address, broker_port)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert frame to bytes
    buffer = cv2.imencode('.jpg', frame)[1].tobytes()

    # Publish frame to MQTT topic
    client.publish(topic, buffer)

    # Wait for a while before publishing next frame
    time.sleep(0.1)

# Release the webcam and disconnect MQTT client
cap.release()
client.disconnect()
