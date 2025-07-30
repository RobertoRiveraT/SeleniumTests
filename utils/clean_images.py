import os
import shutil

def clean_images_folder():
    images_dir = os.path.join(os.getcwd(), "images")

    if not os.path.exists(images_dir):
        print("La carpeta 'images' no existe.")
        return

    for item in os.listdir(images_dir):
        item_path = os.path.join(images_dir, item)

        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # borra archivo o enlace
                print(f"Archivo eliminado: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # borra carpeta
                print(f"Carpeta eliminada: {item_path}")
        except Exception as e:
            print(f"No se pudo eliminar {item_path}: {e}")

if __name__ == "__main__":
    clean_images_folder()
