import streamlit as st
import cv2
import numpy as np
from PIL import Image

def face_detection():
    st.title("Face Detection")

    # Sidebar for adjustable parameters
    with st.sidebar.expander(label="Parameter Settings", icon=":material/settings:"):
        scale_factor = st.slider("Scale Factor", 1.1, 2.0, 1.1, 0.1)
        min_neighbors = st.slider("Min Neighbors", 3, 10, 5, 1)
    
    # Function to detect faces using Haarcascade
    def detect_faces_haarcascade(image, scale_factor, min_neighbors):
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors)
        return faces

    # Function to draw rectangles around faces
    def draw_faces(image, faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image

    # Create tabs
    tab1, tab2 = st.tabs(["Camera Input", "Upload Photo"])

    with tab1:
        st.header("Capture a Photo using Camera")
        camera_photo = st.camera_input("Take a Photo")
        if camera_photo is not None:
            img = Image.open(camera_photo)
            img_array = np.array(img)
            faces = detect_faces_haarcascade(img_array, scale_factor, min_neighbors)
            if len(faces) == 0:
                st.warning("No faces detected.")
            else:
                st.success(f"Number of faces detected: {len(faces)}")
                image_with_faces = draw_faces(img_array.copy(), faces)
                st.image(image_with_faces, caption='Detected Faces', use_column_width=True)

                # Download option
                if st.download_button(
                    label="Download Image with Detected Faces",
                    data=Image.fromarray(image_with_faces).tobytes(),
                    file_name="detected_faces_camera.png",
                    mime="image/png",
                    key="camera_download_button"
                ):
                    result = Image.fromarray(image_with_faces)
                    result.save("detected_faces_camera.png")
        else:
            st.info("Please capture a photo to detect faces.")

    with tab2:
        st.header("Upload a Photo from File")
        uploaded_file = st.file_uploader("Upload a Photo", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            image_array = np.array(image)
            faces = detect_faces_haarcascade(image_array, scale_factor, min_neighbors)
            if len(faces) == 0:
                st.warning("No faces detected.")
            else:
                st.success(f"Number of faces detected: {len(faces)}")
                image_with_faces = draw_faces(image_array, faces)
                st.image(image_with_faces, caption='Detected Faces', use_column_width=True)

                # Download option
                if st.download_button(
                    label="Download Image with Detected Faces",
                    data=Image.fromarray(image_with_faces).tobytes(),
                    file_name="detected_faces_upload.png",
                    mime="image/png",
                    key="upload_download_button"
                ):
                    result = Image.fromarray(image_with_faces)
                    result.save("detected_faces_upload.png")
        else:
            st.info("Please upload a photo to detect faces.")

face_detection()
