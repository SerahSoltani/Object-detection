# YOLOv5 Object Detection on Videos/Images

This project demonstrates the use of the YOLOv5 model for performing object detection on a video or image. The detections are rendered on the frames, and the processed video is saved to disk. The implementation uses the `torch` library for loading the YOLOv5 model and `OpenCV` for video processing.

## Features

- Detects objects in real-time on videos or images.
- Outputs an annotated video with bounding boxes and labels.
- Provides an optional display of the detection process in a window.

## Requirements

To run this code, you need the following dependencies:

- Python 3.7+
- PyTorch
- OpenCV
- YOLOv5 (loaded via `torch.hub`)

Install the dependencies using:

```bash
pip install torch torchvision opencv-python
