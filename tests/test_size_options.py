# tests/test_size_options.py

import os
import shutil
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.penguin_creator_page import PenguinCreatorPage
from utils.image_utils import wait_and_rename_image, DOWNLOAD_DIR
from utils.image_hash_checker import all_image_hashes_unique

SIZE_TEST_DIR = os.path.join(os.getcwd(), "images", "size_test")

@pytest.fixture
def driver():
    options = Options()
    prefs = {"download.default_directory": SIZE_TEST_DIR}
    options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("index", [0, 1, 2])  # 3 tamaños
def test_download_by_size(driver, index):
    page = PenguinCreatorPage(driver)
    page.load()

    time.sleep(2)
    page.open_size_menu()
    time.sleep(1)
    page.select_size_by_index(index)
    time.sleep(1)
    page.click_volver()
    time.sleep(1)

    page.download_image()
    new_name = f"pinguino_size_{index + 1}.png"
    path = wait_and_rename_image(
        old_name="pinguino.png",
        new_name=new_name,
        folder=SIZE_TEST_DIR
    )
    print(f"✅ Imagen guardada como {new_name}")
    assert os.path.exists(path)

    # Al final del último test (index 2), validar que todos sean distintos
    if index == 2:
        assert all_image_hashes_unique(SIZE_TEST_DIR), "❌ Al menos dos tamaños generaron la misma imagen."

