from PIL import Image
import os

def resize_and_overwrite(image_path, size):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.LANCZOS)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(image_path)

# Ejemplo de uso
clase = "Arachnida"
orden = "Amblypygi"
input_dir = f'/home/adrian/Desktop/Datatsets/{clase}/{orden}'
size = (224, 224)

for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        resize_and_overwrite(os.path.join(input_dir, filename), size)
