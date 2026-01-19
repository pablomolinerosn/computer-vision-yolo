# 🚀 Computer Vision with YOLO

Usa un modelo preentrenado para detectar objetos en tiempo real con **OpenCV** y **YOLO v8**

### 📂 Project Structure

- `src/`: Código fuente principal con manejo de logs y excepciones.
- `models/`: Directorio destinado a los pesos del modelo (`.pt`).
- `data/`: Imágenes y videos de muestra para pruebas de inferencia.

### 📊 Model Performance

Se seleccionó la versión **Nano (YOLOv8n)** por su equilibrio entre precisión y latencia en dispositivos de consumo (laptops).

| Model       | Size (px) | mAP50 (COCO) | Speed (CPU ms) |
| :---------- | :-------- | :----------- | :------------- |
| **YOLOv8n** | 640       | 37.3         | ~12.5          |
| **YOLOv8s** | 640       | 44.9         | ~25.4          |

### 🛠️ Tech Stack

- **Core:** Python 3.9+
- **Framework:** Ultralytics (YOLO v8/v9)
- **Vision:** OpenCV-Python
- **Environment:** Virtualenv / Pip

---

### 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/pablomolinerosn/computer-vision-yolo.git](https://github.com/pablomolinerosn/computer-vision-yolo.git)
   cd computer-vision-yolo
   cd src
   python main.py
   ´´´

   Controls: Press 'q' to close the camera window.
   ```

🧠 Model Details
This project uses the Ultralytics framework, leveraging the COCO dataset which can identify up to 80 different classes including people, cars, and electronics.
