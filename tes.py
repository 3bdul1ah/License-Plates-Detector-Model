import os
from ultralytics import YOLO
import cv2
import requests
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

# URL list containing image URLs
image_urls = [
    'https://source.roboflow.com/dRDeH1hYd0WQDBtCSKP39MHuZOY2/bOSrFqHMrIm6IyajhOX8/original.jpg',
    # Add more image URLs here
]

model_path = os.path.join('.', 'runs', 'detect', 'train18', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.6

# List of specific class names to print
specific_classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
state_classes= ['exp', 'new_DUBAI', 'new_RAK', 'new_abudabi', 'new_ajman', 'new_am', 'new_fujairah', 'old_DUBAI', 'old_RAK', 'old_abudabi', 'old_ajman', 'old_am', 'old_fujira', 'old_sharka']

for image_url in image_urls:
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_COLOR)

        H, W, _ = image.shape

        results = model(image)[0]

        # Sort the results by the x-axis position
        sorted_results = sorted(results.boxes.data.tolist(), key=lambda x: x[0])

        specific_class_detected = False
        state_class_detected = False

        for x1, y1, x2, y2, score, class_id in sorted_results:
            class_name = model.names[class_id]
            if score > threshold:
                if class_name in specific_classes:
                    specific_class_detected = True
                    print (class_name, end=' ')

        for x1, y1, x2, y2, score, class_id in sorted_results:
            class_name = model.names[class_id]
            if score > threshold:
                if class_name in state_classes:
                    specific_class_detected = True
                    print (f"\nThis car belongs to {class_name}")

        plt.figure()
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.show()

    else:
        print(f"Failed to retrieve image from URL: {image_url}")
