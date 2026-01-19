# 🚀 Computer Vision with YOLO

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-success)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-red)
![License](https://img.shields.io/badge/license-MIT-green)

Este proyecto implementa detección de objetos en tiempo real utilizando el framework **Ultralytics** y **OpenCV**.

---

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

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Prepare the model:**

   Descarga yolov8n.pt y colócalo en la carpeta /models. El script está configurado para carga local por seguridad y eficiencia.

5. **Execute:**
   ```bash
   cd src
   python main.py

---

### ❗Troubleshooting

- Cámara no detectada: Si usas una cámara externa, cambia cv2.VideoCapture(0) por 1 o 2 en src/main.py.
- Error de Ruta: Asegúrate de ejecutar el script desde la carpeta src para que la ruta relativa ../models/ funcione correctamente.


### 🧠 Model Details
Este proyecto utiliza el framework Ultralytics, aprovechando el conjunto de datos COCO, el cual puede identificar hasta 80 clases diferentes, incluyendo personas, automóviles y dispositivos electrónicos.
