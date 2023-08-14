import cv2

# Load YOLO pre-trained model for vehicle detection
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the COCO names file (contains class names)
classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Load the image
image_path = "path_to_your_image.jpg"
image = cv2.imread(image_path)

# Get image dimensions
height, width, _ = image.shape

# Preprocess the image for YOLO
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# Set input blob for the network
net.setInput(blob)

# Get output layer names
output_layers = net.getUnconnectedOutLayersNames()

# Perform forward pass and get detections
detections = net.forward(output_layers)

# Loop through detections
for detection in detections:
    for obj in detection:
        scores = obj[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        
        if confidence > 0.5 and class_id == 2:  # Class ID for cars is 2
            center_x = int(obj[0] * width)
            center_y = int(obj[1] * height)
            w = int(obj[2] * width)
            h = int(obj[3] * height)
            
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with detections
cv2.imshow("Vehicle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
