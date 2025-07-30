# tests/test_download.py

import os
import shutil
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.penguin_creator_page import PenguinCreatorPage
from utils.image_utils import wait_and_rename_image

DOWNLOAD_DIR = os.path.join(os.getcwd(), "images")

@pytest.fixture
def driver():
    # Crear carpeta de descargas si no existe
    if os.path.exists(DOWNLOAD_DIR):
        shutil.rmtree(DOWNLOAD_DIR)
    os.makedirs(DOWNLOAD_DIR)

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": DOWNLOAD_DIR}
    options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_download_penguin(driver):
    page = PenguinCreatorPage(driver)
    page.load()
    time.sleep(2)  # Esperar por si hay animaciones
    page.download_image()
    renamed_path = wait_and_rename_image()
    assert os.path.exists(renamed_path)

    # Esperar que aparezca la imagen
    for _ in range(20):
        files = os.listdir(DOWNLOAD_DIR)
        pngs = [f for f in files if f.endswith(".png")]
        if pngs:
            print(f"✅ Imagen descargada: {pngs[0]}")
            return
        time.sleep(0.5)

    raise AssertionError("❌ No se descargó ninguna imagen")
