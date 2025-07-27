# 🗑️ Trash Detection Using YOLOv8

This project is a real-time trash object detection system powered by YOLOv8. It leverages the [TACO (Trash Annotations in Context)](https://tacodataset.org/) dataset, with labels in YOLO format, to detect and classify various types of litter such as plastic bottles, batteries, aluminum foil, and more.

---

## 🚀 Features

- 🔍 **Real-time Trash Detection** using a custom-trained YOLOv8 model.
- 📸 Upload images and see object predictions instantly.
- 📦 Detects multiple trash classes including:
  - Plastic bottles
  - Cartons
  - Food waste
  - Bottle caps
  - And many more (based on the TACO dataset).
- 📊 Powered by Ultralytics YOLOv8 with high accuracy and speed.
- 🌐 Streamlit web interface for easy interaction.

---

## 🖼️ Detection Preview

| Uploaded Image |
|----------------|------------------|
| <img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/98796d97-ff6d-414c-adec-b8ecbf65626b" />
| Trash Detected |
|----------------|------------------|
 <img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/a9555bba-e1cf-4c93-b256-17054f2653ef" />

> 📌 Example shows detection of plastic bottle, paper, and wrappers.


## 🧠 Model Details

- **Architecture**: YOLOv8 (Ultralytics)
- **Dataset**: TACO - Trash Annotations in Context
- **Input Size**: 640×640
- **Output**: Bounding boxes + Class labels
- **Model File**: `best.pt` trained on custom dataset


Feel free to contribute or use this model to support waste detection, recycling initiatives, or smart bin automation!
