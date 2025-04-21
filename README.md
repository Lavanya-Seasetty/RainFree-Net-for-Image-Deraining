# RainFree-Net: Image-Deraining
Rain-Free-Net is a deep learning-based image deraining model designed to remove rain streaks from images, improving visibility and clarity. The model uses Convolutional Neural Networks (CNNs) and achieves excellent results in real-time applications like autonomous driving and surveillance.

## Project Structure
- **Train_Dataset/**: Contains the training images (if publicly available).
- **Test_Dataset/**: Contains test images for evaluation.
- **Outputs/**: Shows before-and-after images of derained results.
- **Code/**: Contains the model training, testing, and evaluation scripts.

## Installation
To use this project, you'll need to install the following dependencies:
- Python 
- PyTorch
- OpenCV
- torch==1.5.0
- torchvision==0.5.0
- numpy
- matplotlib
- PIL
- scikit-image
- scipy
- Pillow

## How to Run
1. Clone this repository.
2. Download the **Rain100H dataset** or give your own dataset.
3. Run the training script to train the model.
4. Use the test script to evaluate the model and generate output images.

## Example Outputs
- Before Rain:
  ![Before Rain](Outputs/before_rain_image_1.jpg)
- After Rain-Free:
  ![After Rain-Free](Outputs/after_rain_image_1.jpg)
