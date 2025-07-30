# utils/image_hash_checker.py

import os
from PIL import Image
import imagehash

def all_image_hashes_unique(folder_path):
    hashes = set()
    collisions = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(".png"):
            full_path = os.path.join(folder_path, file)
            with Image.open(full_path) as img:
                h = str(imagehash.average_hash(img))
                if h in hashes:
                    collisions.append(file)
                else:
                    hashes.add(h)

    if collisions:
        print(f"❌ Imágenes duplicadas encontradas: {collisions}")
        return False

    print("✅ Todos los hashes de imagen son únicos.")
    return True
