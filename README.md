# RainFree-Net: Image-Deraining
Rain-Free-Net is a deep learning-based image deraining model designed to remove rain streaks from images, improving visibility and clarity. The model uses Convolutional Neural Networks (CNNs) and achieves excellent results in real-time applications like autonomous driving and surveillance.

# Before Deraining the input image is:
![input_image](https://github.com/user-attachments/assets/5cc66108-d305-4aa2-a545-ad2013d73c48)

# After Deraining:
![output_image](https://github.com/user-attachments/assets/f99bb321-bde3-4820-9b6f-a1f9aa2382ee)

## Project Structure
- **Train_Dataset**: Contains **heavy rain images** used for training the model.
- **Test_Dataset**: Contains **test images** used to evaluate the model’s performance.
- **Val Datset**:Contains **validation images** used during training to tune the model.
- **Code**: Contains scripts for **training**, **testing**, and **evaluating** the model's performance.
  
## Installation
To use this project, you'll need to install the following dependencies:
- Python 
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

