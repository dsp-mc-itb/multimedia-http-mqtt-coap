import cv2
import numpy as np
import paho.mqtt.client as mqtt

# MQTT Broker details
broker_address = "your_broker_ip"
broker_port = 1883
topic = "webcam"

# Function to handle MQTT messages
def on_message(client, userdata, msg):
    # Convert received bytes to numpy array
    nparr = np.frombuffer(msg.payload, np.uint8)

    # Decode the image
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Display the frame
    cv2.imshow('Webcam Stream', frame)
    cv2.waitKey(1)

# Connect to MQTT broker and subscribe to topic
client = mqtt.Client("webcam_subscriber")
client.connect(broker_address, broker_port)
client.subscribe(topic)
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
