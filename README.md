# Multiple_Disease_predictive_system


## Overview
The **Multiple Disease Prediction System** is a web-based application that allows users to predict the likelihood of three different diseases:

1. **Diabetes**
2. **Heart Disease**
3. **Parkinson's Disease**

The application is built using **Streamlit** and leverages machine learning models trained on medical datasets to provide predictions.

---

## Features
- **Diabetes Prediction**: Predicts whether a person is diabetic based on input features such as pregnancies, glucose level, blood pressure, and BMI.
- **Heart Disease Prediction**: Predicts the presence of heart disease using parameters like age, sex, chest pain type, resting blood pressure, cholesterol, and more.
- **Parkinson's Disease Prediction**: Detects Parkinson's disease based on voice-related features like jitter, shimmer, and fundamental frequency.

---

## Tech Stack
- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Machine Learning Models**: Pre-trained models loaded using `pickle`
- **Frontend Components**: Streamlit widgets (text input, select box, buttons)

---

## Prerequisites
Ensure you have the following installed on your system:

1. **Python 3.x**
2. **Streamlit**
3. **Pickle** (for loading saved models)

You can install the required packages using:
```bash
pip install streamlit streamlit-option-menu
```

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Platinumgai/Multiple_Disease_predictive_system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd multiple-disease-prediction
   ```

3. Ensure the saved models (`diabetes.sav`, `heart.sav`, and `parkinson.sav`) are present in the project directory.

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501` to access the application.

---

## Usage
### Sidebar Navigation
The sidebar provides navigation between the three prediction modules:

1. **Diabetes Prediction**
   - Input fields: Number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, and diabetes pedigree function.
   - Click on **"Diabetes Test Result"** to get the prediction.

2. **Heart Disease Prediction**
   - Input fields: Age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, and others.
   - Click on **"Heart Disease Test Result"** to get the prediction.

3. **Parkinson's Prediction**
   - Input fields: Various voice measurement parameters such as MDVP:Fo(Hz), MDVP:Fhi(Hz), jitter, shimmer, and others.
   - Click on **"Parkinson's Test Result"** to get the prediction.

---

## File Structure
```
multiple-disease-prediction/
├── app.py                  # Main application file
├── diabetes.sav            # Saved model for diabetes prediction
├── heart.sav               # Saved model for heart disease prediction
├── parkinson.sav           # Saved model for Parkinson's prediction
└── README.md               # Documentation file
```

---

## Machine Learning Models
### 1. Diabetes Prediction Model
- **Model Type**: Logistic Regression
- **Features Used**:
  - Number of pregnancies
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI
  - Diabetes pedigree function

### 2. Heart Disease Prediction Model
- **Model Type**: Random Forest Classifier
- **Features Used**:
  - Age
  - Sex
  - Chest pain type
  - Resting blood pressure
  - Serum cholesterol
  - Fasting blood sugar
  - Resting electrocardiographic results
  - Maximum heart rate achieved
  - Exercise-induced angina
  - ST depression induced by exercise
  - Slope of the peak exercise ST segment
  - Number of major vessels colored by fluoroscopy
  - Thalassemia

### 3. Parkinson's Prediction Model
- **Model Type**: Support Vector Machine (SVM)
- **Features Used**:
  - MDVP:Fo(Hz)
  - MDVP:Fhi(Hz)
  - MDVP:Flo(Hz)
  - MDVP:Jitter(%)
  - MDVP:Jitter(Abs)
  - MDVP:RAP
  - MDVP:PPQ
  - Jitter:DDP
  - MDVP:Shimmer
  - MDVP:Shimmer(dB)
  - Shimmer:APQ3
  - Shimmer:APQ5
  - MDVP:APQ
  - Shimmer:DDA
  - NHR
  - HNR
  - RPDE
  - DFA
  - Spread1
  - Spread2
  - D2
  - PPE

---

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to report a bug, feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgements
- **Streamlit** for providing an easy-to-use framework for building web applications.
- **Scikit-learn** for the machine learning models.
- Datasets used for training the models are publicly available on platforms like Kaggle and UCI Machine Learning Repository.

---

## Contact
For any inquiries, please contact:
- **Name**: [Nagendla Pedda Babu]
- **Email**: [nagendla.sunny2021@gmail.com]
- **GitHub**: [https://github.com/Platinumgai]

