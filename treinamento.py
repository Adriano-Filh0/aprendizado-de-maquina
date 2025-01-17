from ultralytics import YOLO

model = YOLO("yolo11x.pt")
# treinamento
model.train(data="/home/adriano/am/data_4/Fire-Extinguisher-Detect-1/data.yaml",
            epochs=40,
            imgsz=640,
            device=0)
