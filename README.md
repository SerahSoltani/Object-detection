# Security Camera Object Detection
This project uses YOLOv5 for real-time object detection in security camera footage. The system identifies objects like vehicles, pedestrians, and more to enhance surveillance capabilities.  

## Features
- Real-time detection from video streams or images.
- Outputs bounding boxes with class labels and confidence scores.
- Customizable for additional classes.
  
OpenCV DNN Module
The OpenCV DNN (Deep Neural Network) module is a part of the OpenCV library that enables the use of deep learning models for computer vision tasks. This module is specifically designed for running pre-trained neural network models from popular frameworks like Caffe, TensorFlow, PyTorch, and Darknet.

Key Features of OpenCV DNN
Support for Pre-trained Models:

You can load pre-trained models from frameworks such as:  
YOLO (You Only Look Once) for object detection  
SSD (Single Shot MultiBox Detector)  
Faster R-CNN  
Models from TensorFlow, Caffe, and ONNX format.  

Model Conversion:  
OpenCV DNN supports converted models like ONNX, allowing you to run models created in other frameworks.  

Optimization:  
Designed for real-time processing with support for hardware acceleration (e.g., GPU).
It supports computational libraries like OpenCL and CUDA for enhanced performance.
Image Processing Support:

Includes utilities for preprocessing input images, such as resizing, normalization, and creating blobs.  

Use Cases  
Object Detection: Frameworks like YOLO and SSD.
Image Segmentation: Networks like U-Net.
Face Detection: Models such as Haar cascades or deep learning-based detectors.
Image Classification: Predicting classes for input images.




## Requirements
- Python 3.8+
- PyTorch
- OpenCV
- Torch Hub

## Installation
1. Clone the repository:
   
**Note: Compatability with Python 2.x is not officially tested.**

