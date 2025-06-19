# Multiple Disease Prediction System using Machine Learning

![image](https://github.com/user-attachments/assets/3f680f56-c96d-4a94-b70e-44a7cf6dc7a7)


This project provides a streamlit web application for predicting multiple diseases, including Kidney, Parkinson's disease, and liver disease, using machine learning algorithms. The prediction models are deployed using Streamlit, a Python library for building interactive web applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Multiple Disease Prediction project aims to create a user-friendly web application that allows users to input relevant medical information and receive predictions for different diseases. The machine learning models trained on disease-specific datasets enable accurate predictions for kidney, Parkinson's disease, and liver disease.

## Features

The Multiple Disease Prediction web application offers the following features:

- **User Input**: Users can input their medical information, including age, blood pressure, sugar levels, and other relevant factors.
- **Disease Prediction**: The application utilizes machine learning models to predict the likelihood of having liver, Parkinson's disease, and kidney disease based on the entered medical data.
- **Prediction Results**: The predicted disease outcomes are displayed to the user, providing an indication of the probability of each disease.
- **Visualization**: Visualizations are generated to highlight important features and provide insights into the prediction process.
- **User-Friendly Interface**: The web application offers an intuitive and user-friendly interface, making it easy for individuals without technical knowledge to use the prediction tool.

## Setup

To use this project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/krisv8/Multiple-Disease-Analysis.git
```

2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

3. Download the pre-trained machine learning models for kidney, Parkinson's disease, and liver disease. Make sure to place them in the appropriate directories within the project structure.

4. Update the necessary configurations and file paths in the project files.

## Usage

To run the Multiple Disease Prediction web application, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the Streamlit application:

```bash
streamlit run Multiple_Disease.py
```

3. Access the web application by opening the provided URL in your web browser.

4. Input the relevant medical information as requested by the application.

5. Click the "%Test Result" button to generate predictions for liver/kidney/Parkinson's disease based on the provided data.

6. View the prediction results and any accompanying visualizations or insights.

## Contributing

This is project has been created with some references from google.
