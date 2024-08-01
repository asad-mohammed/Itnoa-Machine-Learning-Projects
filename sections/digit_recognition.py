import streamlit as st
import numpy as np
import pickle
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

def digit_recognition():
    # Load the trained model
    with open('models/digit_recognition_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Function to preprocess the drawn image
    def preprocess_image(image):
        # Convert to grayscale and resize to 8x8
        image = ImageOps.grayscale(image)
        image = image.resize((8, 8))
        image_array = np.array(image)

        # Invert colors: streamlit-drawable-canvas draws in white (255), we need black (0)
        image_array = 255 - image_array

        # Scale pixel values to match the digits dataset
        image_array = image_array / 16.0

        # Flatten the array to match the input format of the model
        image_array = image_array.flatten().reshape(1, -1)
        return image_array

    # Streamlit application
    st.title("Digit Recognition")
    st.write("**Draw any digit (0-9) in the below Canvas** (Use the whole canvas for drawing):")

    col1, col2 = st.columns(2)
    with col1:
        # Create a canvas component
        canvas_result = st_canvas(
            fill_color="white",
            stroke_width=20,
            stroke_color="black",
            background_color="white",
            update_streamlit=True,
            height=300,
            width=300,
            drawing_mode="freedraw",
            key="canvas",
            display_toolbar=True,  # Include the toolbar
            initial_drawing=None,
        )

        if st.button("Predict"):
            with col2:
                if canvas_result.image_data is None or np.all(canvas_result.image_data == 255):
                    st.warning("Please draw a digit before predicting.")
                else:
                    # Preprocess the image
                    img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
                    img = img.convert("L")  # Convert to grayscale
                    preprocessed_image = preprocess_image(img)
                    # Predict the digit
                    prediction = model.predict(preprocessed_image)
                    st.success(f"Predicted Digit: {prediction[0]}")

digit_recognition()
