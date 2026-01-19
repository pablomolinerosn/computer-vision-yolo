import cv2
import os
import logging
from ultralytics import YOLO

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_detection():
    # Obtenemos la ruta raíz del proyecto para localizar el modelo en /models
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, '..', 'models', 'yolov8n.pt')

    # Carga del modelo con manejo de errores
    try:
        logger.info(f"Cargando modelo desde: {model_path}")
        model = YOLO(model_path)
    except Exception as e:
        logger.error(f"No se pudo cargar el modelo. Verifica que el archivo existe en /models. Error: {e}")
        return

    # Inicialización de la cámara
    cap = cv2.VideoCapture(0) # 0 es la cámara integrada
    
    if not cap.isOpened():
        logger.error("Error: No se pudo acceder a la cámara de la laptop.")
        return

    logger.info("Iniciando detección en tiempo real. Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.warning("No se pudo recibir el frame de la cámara. Finalizando...")
            break

        # Inferencia
        # stream=True utiliza un generador para ahorrar memoria RAM
        results = model(frame, stream=True, verbose=False)

        # Visualización
        for r in results:
            annotated_frame = r.plot()

        cv2.imshow('YOLO Real-Time Detection', annotated_frame)

        # Salida limpia con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("Cerrando aplicación por el usuario.")
            break

    # Liberación de recursos
    cap.release()
    cv2.destroyAllWindows()
    logger.info("Recursos liberados correctamente.")

if __name__ == "__main__":
    run_detection()