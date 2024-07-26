import streamlit as st
import time

def face_detection_info():
    st.title("Face Detection Information")

    # Introduction
    st.header("Introduction")
    st.write("""
    This project utilizes a face detection model to identify faces in images.
    The model is built using OpenCV's Haarcascade, a pre-trained classifier for detecting faces.
    Users can capture photos using their camera or upload existing photos, and the model will identify and highlight any faces detected in the images.
    The adjustable parameters in the sidebar allow fine-tuning of the face detection process.
    """)

    # Code Explanation
    st.header("Code Explanation")
    st.write("""
    The main steps in the code are as follows:
    1. **Setting up the Streamlit app**: The app is set up with a title and a sidebar for parameter settings.
    2. **Parameter Settings**: Users can adjust the `Scale Factor` and `Min Neighbors` parameters using sliders in the sidebar.
    3. **Face Detection Function**: The function `detect_faces_haarcascade` uses OpenCV's Haarcascade to detect faces in an image.
    4. **Drawing Faces**: The function `draw_faces` draws rectangles around detected faces in the image.
    5. **Tabs for Input Methods**: Two tabs are created for different input methods: capturing a photo using the camera and uploading a photo from the file system.
    6. **Camera Input**: Users can capture a photo using their camera, and the app will detect and display faces in the captured image.
    7. **File Upload**: Users can upload a photo from their file system, and the app will detect and display faces in the uploaded image.
    8. **Download Options**: After detecting faces, users can download the image with highlighted faces.
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    This project showcases a simple yet effective face detection application using OpenCV's Haarcascade classifier. 
    The adjustable parameters allow users to fine-tune the detection process, making the model more versatile and adaptable to different conditions. 
    Users can either capture a photo using their camera or upload an existing photo to detect faces. 
    The application provides an easy-to-use interface for face detection, making it accessible for various use cases.
    """)

    st.write("To run the model click the button below")
    if st.button(label= ":blue[**Run Face Detection**]"):
        st.switch_page("sections/face_detection.py")

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
