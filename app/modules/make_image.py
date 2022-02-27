import matplotlib
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import io 
from PIL import Image

def make_image(image, model_response, filename):
    # We display bounding boxes and the class label with the predicted probability for each object.
    # Get the image height and width
    image = Image.open(image)
    image_width, image_height = image.size
    # Create figure and axes
    fig, ax = plt.subplots()
    # Set larger figure size
    fig.set_dpi(600)
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
    plt.savefig(filename, format = 'png')

