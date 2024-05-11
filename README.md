# Brain Tumor Detection and Classification By Using CNN

This repository contains the Python source code and Jupyter notebooks for the Bachelor's thesis titled "Brain Tumor Detection and Classification Using CNN," developed by MD KAMRUL ISLAM under the supervision of Prof. Chen Jie.

## Overview

This project aims to enhance the accuracy of brain tumor detection through advanced Convolutional Neural Networks (CNNs). Utilizing T1-weighted contrast-enhanced MRI images, the CNN model classifies tumors into four categories: meningioma, glioma, pituitary tumor, and no tumor. Our model outperforms traditional models with higher accuracy and lower computational demands.



## Usage

To run the model, open the trained_cnn_model.ipynb in Jupyter Notebook or JupyterLab and execute the cells sequentially. Ensure that the dataset is located in the correct directory as specified in the notebook.

## Data

The dataset comprises MRI images that have been preprocessed and augmented to improve model training efficacy. Due to privacy and size considerations, the dataset is not publicly available in this repository.

## Models

This project utilizes various CNN architectures, including custom models and pretrained models such as VGG-16, Xception, ResNet50, and Inception-V3. Each model's performance is evaluated based on its accuracy in classifying the MRI images into the correct tumor categories.

## Results

Our CNN model achieved a validation accuracy surpassing traditional architectures like VGG-16 (94%), Xception (97%), ResNet-50 (94%), and Inception-V3 (96%).

## Repository Structure

```plaintext
/
├── src/
│   ├── trained_cnn_model.ipynb 
│   └── data_preprocessing.py  # Data preprocessing scripts
└── README.md
