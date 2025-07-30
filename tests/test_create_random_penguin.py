import os
import shutil
import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.penguin_creator_page import PenguinCreatorPage
from utils.image_utils import wait_and_rename_image

RANDOM_TEST_DIR = os.path.join(os.getcwd(), "images", "random_test")

@pytest.fixture
def driver():
    if os.path.exists(RANDOM_TEST_DIR):
        shutil.rmtree(RANDOM_TEST_DIR)
    os.makedirs(RANDOM_TEST_DIR)

    options = Options()
    prefs = {"download.default_directory": RANDOM_TEST_DIR}
    options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def select_random_option_from_menu(page, menu_text):
    # Abrir el menú
    WebDriverWait(page.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[.//p[text()='{menu_text}']]"))
    ).click()

    # Esperar y obtener todos los botones visibles
    options = WebDriverWait(page.driver, 10).until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "div[style*='opacity: 1'] > div.relative > button"
        ))
    )

    if not options:
        raise Exception(f"No options found for menu: {menu_text}")

    random.choice(options).click()

    # Clic en "Volver"
    WebDriverWait(page.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Volver')]"))
    ).click()

    time.sleep(1)

def test_create_random_penguin(driver):
    page = PenguinCreatorPage(driver)
    page.load()
    time.sleep(2)

    # Menús visuales detectables por texto
    menus = [
        "Tamaño", "Colores", "Ojos", "Tatuajes",
        "Accesorios", "Ropa", "Cabello", "Sombreros", "Objetos"
    ]

    for menu in menus:
        select_random_option_from_menu(page, menu)

    time.sleep(1)
    page.download_image()

    image_path = wait_and_rename_image(
        old_name="pinguino.png",
        new_name="random_penguin_1.png",
        folder=RANDOM_TEST_DIR
    )
    assert os.path.exists(image_path)
