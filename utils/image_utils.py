# utils/image_utils.py

import os
import time
import shutil

DOWNLOAD_DIR = os.path.join(os.getcwd(), "images")

def wait_and_rename_image(old_name="pinguino.png", new_name="nuevo.png", folder=DOWNLOAD_DIR, timeout=10):
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    for _ in range(timeout * 2):
        if os.path.exists(old_path):
            break
        time.sleep(0.5)
    else:
        raise Exception(f"No se encontró el archivo {old_name} después de {timeout} segundos")

    if os.path.exists(new_path):
        os.remove(new_path)

    shutil.move(old_path, new_path)

    print(f"✅ Imagen renombrada: {new_name}")
    return new_path
