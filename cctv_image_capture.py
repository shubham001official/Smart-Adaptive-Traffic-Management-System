import cv2
import time

def capture_image(camera_index, output_path):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame from camera.")
        return
    
    # Save the captured frame as an image
    cv2.imwrite(output_path, frame)
    
    # Release the camera
    cap.release()
    print("Image captured and saved as", output_path)

def main():
    camera_index = 0  # Change this to the appropriate camera index
    interval_seconds = 5  # Time interval between captures
    
    while True:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_filename = f"captured_image_{timestamp}.jpg"
        
        capture_image(camera_index, image_filename)
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
