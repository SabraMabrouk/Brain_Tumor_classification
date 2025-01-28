# Brain_Tumor_Classification

## Introduction

The goal of this brain tumor classification project is to develop an automated system that can accurately classify brain tumor types from MRI scans. Brain tumors are abnormal growths of tissue within the brain that can be either benign (non-cancerous) or malignant (cancerous). Diagnosing brain tumors accurately is a critical task for medical professionals, as early detection and accurate classification play a significant role in the treatment and prognosis of patients.  

## Objective
Build a deep learning model that can automatically classify brain tumor from MRI scans into categories:
- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

## Content

This repository includes:

- data folder :
    - raw -- original images (training and testing datasets)
    - interim -- loaded adat as tfrecord
    - processed -- processed data
      
- notebooks folder :
    - [Data_wrangling_EDA.ipynb](https://github.com/SabraMabrouk/Brain_Tumor_classification/blob/04b6729ef8e0f4617b605f800eb2012350a80317/notebooks/Data_Wrangling_EDA.ipynb), this step focuses on collecting the data, organizing it, and making sure it's well defined, the data is also explored to better understand it.
    - [Modeling.ipynb](), in this notebook, images were preprocessed (filtered, cropped, transformed to enhance the contrast, normalized, and resized), and a cnn model was built and trained for brain tumor classification. A hyperparameters tuning step is also included along with evaluation.

- models -- results from hyperparameter tuning (for each trial, the configuration of hyperparameters, The trained model's weights and performance metrics are stored)

- metrics.json -- logs for each fold's training process, with each fold having an array of epochs containing the accuracy, loss, validation accuracy, and validation loss for that epoch.

- capstone3.yaml -- used environment

  
  
## Data source
The dataset used in this project is available [here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data).



## Author
Sabra Mabrouk
