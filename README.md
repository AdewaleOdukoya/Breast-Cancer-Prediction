# Breast Cancer Prediction Project
## Table of Contents
1. Project Overview
2. Dataset
3. Installation
4. Usage
5. Model
6. Results
7. Contributing
8. Contact

## Project Overview
This project involves building a machine learning model to predict breast cancer using the Wisconsin Diagnostic Breast Cancer (WDBC) dataset. The primary objective is to classify tumors as malignant or benign based on various features extracted from test parameters taken from patients.
## Dataset
#### Name: Wisconsin Diagnostic Breast Cancer (WDBC)
#### File: wdbc.csv
#### Description: The dataset contains 569 samples of breast tumor biopsies, each with 30 features plus an ID and diagnosis (malignant or benign).
## Installation
#### 1. Clone the repository:
git clone https://github.com/AdewaleOdukoya/Breast-Cancer-Prediction.git
#### 2. Navigate to the project directory:
cd BreastCancerPrediction
#### 3. Install the required packages:
pip install -r requirements.txt
## Usage
#### 1. Running the Notebook:
##### Open Breast Cancer Prediction Project.ipynb using Jupyter Notebook or 
##### Jupyter Lab to explore the data analysis, model training, and evaluation processes.
#### 2. Using the Pre-trained Model:
##### Load the model in your Python environment:
import pickle

with open('BreastCancerProjectapt1.pkl', 'rb') as file:
    model = pickle.load(file)
##### Use the model to make predictions:
predictions = model.predict(your_data)
## Model
##### File: BreastCancerProjectapt1.pkl
##### Description: This is the pre-trained machine learning model for predicting breast cancer 
##### diagnosis. It was trained and evaluated using various algorithms, with the final model chosen 
##### based on performance metrics.
## Results
Detailed results and analysis are provided in the Breast Cancer Aptech1.pdf report. 
This includes performance metrics, visualizations, and insights derived from the model's 
predictions.
## Contributing
##### Contributions are welcome! Please fork the repository and submit a pull request if you have any 
improvements or bug fixes.
## Contact
##### For questions or suggestions, please reach out to:

##### Email: adewaleusmail@gmail.com
##### GitHub: AdewaleOdukoya

