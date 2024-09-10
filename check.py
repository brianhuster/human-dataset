import os
from PIL import Image


def check_labels(label_path):
    try:
        with open(label_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) != 5:  # YOLO format: class x_center y_center width height
                    print(len(parts))
                    return False
                if not (0 <= float(parts[1]) <= 1 and 0 <= float(parts[2]) <= 1 and
                        0 <= float(parts[3]) <= 1 and 0 <= float(parts[4]) <= 1):
                    return False
            return True
    except Exception as e:
        return False


# Iterate over label files in your dataset
img_dir = "test/images"
label_dir = img_dir.replace('/images', '/labels')
for file in os.listdir(label_dir):
    if file.endswith('.jpg'):
        check = check_labels(os.path.join(img_dir.replace(
            '/images', 'labels'), file.replace('.jpg', '.txt')))
        if not check:
            os.remove(os.path.join(img_dir, file))
            os.remove(os.path.join(label_dir, file.replace('.jpg', '.txt')))
