# Fake Email Detector

## Overview
This project is a simple Fake Email (Phishing) Detection system built using Python.
It analyzes email text and classifies it as Spam (Phishing) or Safe (Ham) using both Machine Learning (Logistic Regression) and Rule-based keyword detection.

## Problem Statement
Phishing emails are a common cybersecurity threat. Many users fall victim to fake emails that try to steal sensitive information like passwords, bank details, etc.
This project aims to provide a simple tool that can help identify suspicious emails based on their content.

## Solution
The system combines two approaches:
1. **Machine Learning Model**
   * Uses TF-IDF for text processing
   * Uses Logistic Regression for classification
2. **Rule-Based Detection**
   * Detects suspicious keywords like:
     * "urgent"
     * "click"
     * "free"
     * "password"
       
##  Features
* Detects phishing/spam emails
* Uses Machine Learning for prediction
* Uses rule-based scoring for extra accuracy
* Simple and easy to use
* Beginner-friendly implementation

## Technologies Used
* Python
* Pandas
* Scikit-learn
* Pickle

## Project Structure
fake-email-detector/
├── emails.csv
├── train.py
├── detector.py
├── main.py
├── requirements.txt
└── README.md

## How to Run the Project

### 1. Install dependencies
pip install -r requirements.txt

### 2. Train the model
python train.py

### 3. Run the detector
python main.py

## Example
Input:
Urgent! Click here to verify your bank account

Output:
Spam / Phishing Email

## Future Improvements
* Add GUI using Tkinter
* Use larger dataset for better accuracy
* Add URL/domain analysis
* Deploy as a web application

## What I Learned
* Basics of Machine Learning
* Text processing using TF-IDF
* Model training and saving using pickle
* Combining ML with rule-based systems
* Structuring a real-world project

## Author
Srishti Yadav

This project is for educational purposes only.
