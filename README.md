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
```

## Usage

1. Clone this repository or copy the code into your working directory.

2. Replace the `input_path` with the path to your input video or image.

```python
input_path = 'data/sample_video.mp4'  # Replace with your video or image path
```
   
3. Specify the `output_path` where the processed video will be saved.
   
```python
output_path = 'output/processed_video.mp4'
```
  
4. Run the script:
   
```bash  
python script_name.py
```
  
5. The annotated video will be saved at the specified `output_path`. If a display is active, press 'q' to quit the visualization window.


# Code Overview

- **Load YOLOv5 model**: The YOLOv5 model is loaded using `torch.hub`.
- **Process input**: The script processes video frames or images from the specified `input_path`.
- **Object detection**: The YOLOv5 model detects objects in each frame.
- **Rendering and saving**: Detected objects are annotated, and the resulting frames are saved as a new video.


## License

This project uses the [MIT License](https://opensource.org/licenses/MIT). Refer to the `LICENSE` file for more details.
"""




