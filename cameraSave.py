#Image with the original resolution
import cv2
import streamlit as st
import numpy as np

def main():
    print("hello")
    # st.subheader(f"Click 'Capture Image' to Detect the food")
    
    # Create a VideoCapture object
    cap = cv2.VideoCapture(2)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return
    
    # Create a button to capture the image
    if st.button("Capture Image",type='primary'):
        ret, frame = cap.read()
        if ret:
            # Display the captured image
            st.image(frame, channels="BGR")
            
            # Save the image locally
            filename = "C:\\Users\\rocha\\OneDrive\\Desktop\\calorieNEW\\CalorieDetection\\upload_images\\captureImage\\captureImagecaptured_image.jpg"
            cv2.imwrite(filename, frame)
            st.success(f"Image Saved.")
        else:
            st.error("Error: Could not capture image.")
    
    # Release the VideoCapture object and close the Streamlit app
    cap.release()

if __name__ == "__main__":
    main()
