import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def cancer_prediction_info():
    st.title("Cancer Prediction Information")

    # Introduction
    st.header("Introduction")
    st.write(""" 
    This project aims to train a classifier model on a dataset of cancer cell characteristics to predict whether a cell is benign (B) or malignant (M).
    The model used in this project is a Random Forest classifier, chosen for its robustness and accuracy.
    """)

    # Dataset
    st.header("Dataset")
    st.write("""
    The dataset used in this project was created by the University of Wisconsin and contains 569 instances and 32 attributes. 
    These attributes include the ID number, diagnosis (M = malignant, B = benign), and ten real-valued features computed for each cell nucleus.
    """)

    # Load and display the dataset
    data = pd.read_csv('datasets/data.csv')
    st.write(data)

    st.write("""
    The dataset attributes are as follows:
    1. ID number
    2. Diagnosis (M = malignant, B = benign)
    3. Ten real-valued features computed for each cell nucleus: radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension.
    """)
    st.write("""
    As mentioned in UCI website, “Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image”.
    Moreover, FNA is a type of biopsy procedure where a very thin needle is inserted into an area of abnormal tissue or cells with a guide of CT scan or ultrasound monitors (figure1). The collected sample is then transferred to a pathologist to study it under a microscope and examine whether cells in the biopsy are normal or not.
    """)
    st.image("datasets/fna_ultrasound.jpg", width=500)

    # Code Explanation
    st.header("Code Explanation")
    st.write("""
    The main steps in the code are as follows:
    1. **Loading the trained model**: The trained Random Forest model is loaded from a pickle file.
    2. **Defining feature names**: The features used for prediction are defined.
    3. **Loading sample data**: Sample data is loaded to provide min, max, and mean values for the sliders.
    4. **Collecting user inputs**: Sliders are used to collect user inputs for each feature.
    5. **Making predictions**: The model predicts whether the input features correspond to a benign or malignant cell, and the prediction probabilities are displayed.
    6. **Display the prediction result**: The prediction and prediction probabilities are displayed to the user.
    """)

    # Model Details
    st.header("Model Details")
    st.write("""
    The model used in this project is a Random Forest classifier with the following parameters:
    - Bootstrap: True
    - CCP Alpha: 0.0
    - Class Weight: None
    - Criterion: Gini
    - Max Depth: None
    - Max Features: sqrt
    - Max Leaf Nodes: None
    - Max Samples: None
    - Min Impurity Decrease: 0.0
    - Min Samples Leaf: 1
    - Min Samples Split: 2
    - Min Weight Fraction Leaf: 0.0
    - N Estimators: 500
    - OOB Score: False
    - Random State: 42
    - Verbose: 0
    - Warm Start: False
    
    The model achieved an accuracy of 99.12%.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    This project demonstrates the use of a Random Forest classifier to predict whether a cancer cell is benign or malignant based on cell characteristics. 
    The high accuracy of the model suggests that it can be a useful tool for assisting in the diagnosis of breast cancer. 
    Further improvements can be made by experimenting with different models and parameters, as well as incorporating additional data.
    """)

    st.write("To run the model click the button below")
    if st.button(label= ":blue[**Run Cancer Prediction**]"):
        st.switch_page("sections/cancer_prediction.py")

    # Back to Top Button
    js = '''
    <script>
        var body = window.parent.document.querySelector(".main");
        console.log(body);
        body.scrollTop = 0;
    </script>
    '''

    if st.button(label= ":blue[**Back to top**]"):
        temp = st.empty()
        with temp:
            st.components.v1.html(js)
            time.sleep(.5) # To make sure the script can execute before being deleted
        temp.empty()
