import paho.mqtt.client as mqtt
import tkinter
import threading
import requests
import io 
import json
from PIL import Image
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from tkinter import filedialog
import warnings

global cache_requests

warnings.filterwarnings("ignore")

class client_prediction():
    def __init__(self) -> None:
        mqtt_client = mqtt.Client()
        mqtt_client.on_connect = self.connected
        mqtt_client.on_message = self.message_deliverying
        mqtt_client.connect("localhost", 1883, 5)
        mqtt_client.loop_forever()
        pass

    def connected(self, client, userdata, flags, rc):
        print("Listening callbacks..")
        client.subscribe("predictions")
        
    def message_deliverying(self, client, userdata, msg):
        print("In topic: " + msg.topic + ", message: " +str(msg.payload.decode("utf-8")))
        jsonReq = json.loads(str(msg.payload.decode("utf-8")))
        try:
            make_image(jsonReq['filename'], jsonReq)
        except:
            pass
        finally:
            print("Press enter for call a new prediction...")
        

def make_image(image, model_response):
    image = Image.open(image)
    image_width, image_height = image.size
    # Create figure and axes
    fig, ax = plt.subplots()
    # Set larger figure size
    fig.set_dpi(200)
    # Display the image
    plt.imshow(image)

    # Set up the color of the bounding boxes and text
    color = '#00FF00'
    # For each object, draw the bounding box and predicted class together with the probability
    for prediction in model_response['predictions']:
        bbox = prediction['detection_box']
        # Unpack the coordinate values
        y1, x1, y2, x2 = bbox
        # Map the normalized coordinates to pixel values: scale by image height for 'y' and image width for 'x'
        y1 *= image_height
        y2 *= image_height
        x1 *= image_width
        x2 *= image_width
        # Format the class probability for display
        probability = '{0:.4f}'.format(prediction['probability'])
        # Format the class label for display
        label = '{}'.format(prediction['label'])
        label = label.capitalize()
        # Create the bounding box rectangle - we need the base point (x, y) and the width and height of the rectangle
        rectangle = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor=color, facecolor='none')
        ax.add_patch(rectangle)
        # Plot the bounding boxes and class labels with confidence scores
        plt.text(x1, y1-5, label, fontsize=4, color=color, fontweight='bold',horizontalalignment='left')
        plt.text(x2, y1-5, probability, fontsize=4, color=color, fontweight='bold',horizontalalignment='right')
    plt.axis('off')
    ##buffer = io.BytesIO()
    plt.show()
    
def new_prediction():
    print("Press enter for call a new prediction...")
    input()
    root = tkinter.Tk()
    root.wm_attributes("-topmost", True)
    filename = filedialog.askopenfilename()
    root.destroy()
    payload = {"image" : open(filename, 'rb'),
               "json" : json.dumps({"filename" : filename})}
    
    req = requests.post('http://localhost:80/predict/', files=payload)
    jsonReq = json.loads(req.text)
    jsonReq["filename"] = filename 
    cache_requests.append(jsonReq)

     
cache_requests = list()    
client = threading.Thread(target=client_prediction, args=()).start()
while(True): 
    new_prediction()
