import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time

def cancer_prediction():
    st.title("Cancer Prediction")
    st.markdown("#### **Adjust the values below accordingly to predict**")

    # Load the trained model
    with open('models/cancer_prediction_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Define feature names
    feature_names = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]

    # Load sample data to get min, max, and mean for sliders (assuming data is available in 'data.csv')
    data = pd.read_csv('datasets/data.csv')

    # Collect user inputs using sliders in six columns
    user_inputs = []
    columns = st.columns(5)
    for i, feature in enumerate(feature_names):
        col = columns[i % 5]
        value = col.slider(feature, float(data[feature].min()), float(data[feature].max()), float(data[feature].mean()))
        user_inputs.append(value)

    # Predict using the trained model
    input_data = pd.DataFrame([user_inputs], columns=feature_names)
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Display the prediction result
    st.subheader('Prediction')
    if prediction[0] == 1:
        st.write('The model predicts: **Malignant (Cancer)**')
    else:
        st.write('The model predicts: **Benign (No Cancer)**')

    # Display the prediction probabilities
    st.subheader('Prediction Probabilities')
    st.write(f'Malignant: {prediction_proba[0][1]*100:.2f}%')
    st.write(f'Benign: {prediction_proba[0][0]*100:.2f}%')

cancer_prediction()
