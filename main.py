from ultralytics import YOLO
import cv2
import time
import numpy as np

model = YOLO('yolov8s.pt')

# Initialize webcam
cap = cv2.VideoCapture(0)  # Ustawienie źródła obrazu
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Roździelczość(jakość systemu)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def detect_objects(frame):
    results = model(frame)

    detected_objects = []

    if results and len(results) > 0:
        result = results[0]

        if hasattr(result, 'boxes') and len(result.boxes) > 0:
            for box in result.boxes:
                # koordynaty obiektu
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

                confidence = box.conf[0].cpu().numpy()

                # class name
                class_id = int(box.cls[0].cpu().numpy())
                class_name = model.names[class_id]
                # Kalkulacja środka obiektu (dla targetu robota)
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                # oblicz rozmiar obiektu
                width = int(x2 - x1)
                height = int(y2 - y1)

                # dane obiektu dla robota # TODO: Jaka jest ścieżka komunikacji której można użyć z cobotem
                object_data = {
                    'class': class_name,
                    'confidence': float(confidence),
                    'center': (center_x, center_y),
                    'size': (width, height),
                    'bbox': (int(x1), int(y1), int(x2), int(y2))
                }

                detected_objects.append(object_data)

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (int(x1), int(y1) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return frame, detected_objects
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    start_time = time.time()
    processed_frame, detected_objects = detect_objects(frame)
    fps = 1.0 / (time.time() - start_time)
    cv2.putText(processed_frame, f"FPS: {fps:.2f}", (10, 30), 
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # informacje o obiekcie
    if detected_objects:
        print("Detected objects:")
        for i, obj in enumerate(detected_objects):
            print(f"  {i+1}. {obj['class']} (Conf: {obj['confidence']:.2f}) at {obj['center']}")

    cv2.imshow('YOLOv8 Real-Time Detection', processed_frame)

    # program się zamyka na przycisk "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
