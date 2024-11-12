from ultralytics import YOLO

# Load a model obb 
# model = YOLO('ultralytics\yolov8n.pt')  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data='/home/un/文档/xz/ultralyticsSWIM/ultralytics/ultralytics/cfg/datasets/SWIM-obb.yaml', epochs=100, imgsz=384)


# bones 
model = YOLO('D:/ultralyticsSWIM/ultralyticsSWIM/yolov8n.pt') 
results = model.train(data='D:/ultralyticsSWIM/ultralyticsSWIM/ultralytics/ultralytics/cfg/datasets/bones.yaml', epochs=500, imgsz=384)





