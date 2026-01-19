import os
import cv2
from ultralytics import YOLO

# Obtener la ruta de la carpeta donde se encuentra el modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'models', 'yolov8n.pt')

# Cargar el modelo desde la ruta local
model = YOLO(model_path)

# Inicializar la captura de video (0 cámara integrada de la laptop)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

print("Presiona 'q' para salir.")

while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar la detección en el fotograma actual
    # stream=True es más eficiente para video en tiempo real
    results = model(frame, stream=True)

    # Dibujar los resultados en el fotograma
    for r in results:
        annotated_frame = r.plot()

    # Mostrar el resultado en una ventana
    cv2.imshow('YOLO Real-Time Detection', annotated_frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()