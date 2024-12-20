import torch
import cv2
import os

# Load YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Input video or image
input_path = 'data/sample_video.mp4'  # Replace with your video or image path
output_path = 'output/processed_video.mp4'

# Open video
cap = cv2.VideoCapture(input_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Save output video
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects
    results = model(frame)

    # Render detections
    annotated_frame = results.render()[0]

    # Write to output video
    out.write(annotated_frame)

    # Display (Optional)
    cv2.imshow('Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
