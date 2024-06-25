from ultralytics import YOLO

model = YOLO('yolov8x')

results = model.predict('input_videos/20240519_WUL_SFatSD_left_24_clip.mp4', save=True)
print(results[0])
print("=====================================")
for box in results[0].boxes:
    print(box)