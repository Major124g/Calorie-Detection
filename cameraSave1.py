#Image capture with 224x224 frame size
import cv2
import streamlit as st

def main():
    st.title("Webcam Image Capture")
    
    # Create a VideoCapture object
    cap = cv2.VideoCapture(1)
    
    # Set frame size (optional, adjust as needed)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)  # Width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)  # Height
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return
    
    # Create a button to capture the image
    if st.button("Capture Image"):
        ret, frame = cap.read()
        if ret:
            # Resize the frame (optional, adjust as needed)
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            
            # Display the captured image
            st.image(frame, channels="BGR")
            
            # Save the image locally
            filename = "C:\\Users\\rocha\\OneDrive\\Desktop\\calorieNEW\\CalorieDetection\\upload_images\\captureImage\\captureImagecaptured_image.jpg"
            cv2.imwrite(filename, frame)
            st.success(f"Image saved as {filename}")
        else:
            st.error("Error: Could not capture image.")
    
    # Release the VideoCapture object and close the Streamlit app
    cap.release()

if __name__ == "__main__":
    main()



# import cv2
# import streamlit as st
# import numpy as np

# def main():
#     print("hello")
#     st.title("Webcam Image Capture")
    
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(1)
    
#     # Check if the webcam is opened correctly
#     if not cap.isOpened():
#         st.error("Error: Could not open webcam.")
#         return
    
#     # Create a button to capture the image
#     if st.button("Capture Image"):
#         ret, frame = cap.read()
#         if ret:
#             # Display the captured image
#             st.image(frame, channels="BGR")
            
#             # Save the image locally
#             filename = "C:\\Users\\rocha\\OneDrive\\Desktop\\calorieNEW\\CalorieDetection\\upload_images\\captureImage\\captureImagecaptured_image.jpg"
#             cv2.imwrite(filename, frame)
#             st.success(f"Image saved as {filename}")
#         else:
#             st.error("Error: Could not capture image.")
    
#     # Release the VideoCapture object and close the Streamlit app
#     cap.release()

# if __name__ == "__main__":
#     main()
