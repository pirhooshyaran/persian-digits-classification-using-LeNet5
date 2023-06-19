# Persian Digits Classification using LeNet-5

## Introduction
This repository showcases a simple Computer Vision project that focuses on the classification of Persian digits using the LeNet-5 convolutional neural network architecture, originally proposed by Yann LeCun et al. The goal of this project is to accurately classify handwritten Persian digits from 0 to 9.

## Dataset
The dataset used in this project was created by collecting images of handwritten Persian digits. The digits were written by different individuals on a piece of paper, and then photographs of the digits were taken. The images were organized into a folder structure where each digit class had its own sub-folder within a folder named "raw_images". The sub-folders were labeled from "0" to "9" corresponding to the respective digit class.

Below are instances of raw images showcasing the Persian digits "2" and "6" respectively.

<p align="left">
  <img src="https://github.com/pirhooshyaran/persian-digits-classification-using-LeNet5/blob/master/raw_images/2/001.png" width="100" alt="Number 2">
  <img src="https://github.com/pirhooshyaran/persian-digits-classification-using-LeNet5/blob/master/raw_images/6/001.png" width="100" alt="Number 6">
</p>

To preprocess the dataset, the images were cropped to focus on the digit itself, ensuring that each digit was located in the center of the image. The cropped images were then resized to a uniform size of (32, 32) pixels using the OpenCV library. This resizing step helps to standardize the input size for training the LeNet-5 model.

Additionally, to enhance the quality and improve the accuracy of the model, two additional preprocessing techniques were applied. First, a Gaussian blur filter was applied to reduce noise and smooth out any irregularities or pixel-level variations in the images. This step helps to improve the overall quality and reduce unwanted artifacts.

After the Gaussian blur, a thresholding operation was performed. Thresholding converts the image into a binary form, distinguishing the digit from the background. This segmentation step helps to enhance contrast and isolate the digit from the surrounding elements.

The final dataset looks like the following images which are Persian number "3" and "5" respectively.

<p align="left">
  <img src="https://github.com/pirhooshyaran/persian-digits-classification-using-LeNet5/blob/master/dataset/3/001.png" width="100" alt="Number 2">
  <img src="https://github.com/pirhooshyaran/persian-digits-classification-using-LeNet5/blob/master/dataset/5/001.png" width="100" alt="Number 6">
</p>

The resulting preprocessed images were saved as a new dataset into the "dataset" folder, ready for training the LeNet-5 model.Please refer to the `create_dataset.py` file in the repository for the specific implementation details of the dataset creation process. Additionally, for the testing set, two randomly selected images were chosen from each class and separated into a separate "test_set" folder using the `create_testset.py` file.

The dataset created through these steps provides a diverse and representative collection of handwritten Persian digits, enabling the training and evaluation of the LeNet-5 model for accurate classification.

## Model Architecture
The LeNet-5 architecture, originally proposed by Yann LeCun et al., has proven to be effective in image classification tasks. It consists of multiple convolutional and pooling layers, followed by fully connected layers. For this project, the LeNet-5 architecture was adapted and trained specifically for classifying Persian digits.
![LeNet-5 Architecture](https://github.com/pirhooshyaran/persian-digits-classification-using-LeNet5/blob/master/images/LeNet5_architecture.png)

## Implementation
The project was implemented using TensorFlow and Keras. The training process involves loading the dataset, constructing the LeNet-5 model, training the model on the dataset, and evaluating its performance. Comprehensive explanations and detailed insights can be found within the `persian_digits_classifier.ipynb` notebook, offering a deeper understanding of the project's implementation.