from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('runs/detect/train18/weights/best.pt')

# Define remote image or video URL
source = 'https://source.roboflow.com/dRDeH1hYd0WQDBtCSKP39MHuZOY2/3eO0urIBcEjzYDWshuFg/original.jpg'

# Run inference on the source
results = model(source)  # list of Results objects