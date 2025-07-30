# tests/test_pairwise_penguins.py

import os
import time
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.penguin_creator_page import PenguinCreatorPage
from utils.image_utils import wait_and_rename_image  # <-- Use the helper again
from utils.pairwise_generator import generate_indexed_combinations

# Directory where pairwise images will be stored
PAIRWISE_DIR = os.path.join(os.getcwd(), "images", "pairwise_test")

# Path for the log file
LOG_FILE = os.path.join(PAIRWISE_DIR, "log.txt")

# Category counts: each category has N options (indexed from 0 to N-1)
CATEGORY_COUNTS = {
    "Tamaño": 3,
    "Colores": 10,
    "Ojos": 15,
    "Tatuajes": 16,
    "Accesorios": 15,
    "Ropa": 14,
    "Cabello": 13,
    "Sombreros": 16,
    "Objetos": 11
}

@pytest.fixture(scope="session", autouse=True)
def prepare_folder():
    """
    Ensure the download folder is empty before the tests.
    """
    if os.path.exists(PAIRWISE_DIR):
        shutil.rmtree(PAIRWISE_DIR)
    os.makedirs(PAIRWISE_DIR)

@pytest.fixture
def driver():
    """
    Start a Chrome browser with the custom download directory.
    """
    options = Options()
    prefs = {"download.default_directory": PAIRWISE_DIR}
    options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def select_option_by_index(page, menu_text, index):
    """
    Local helper: open menu by name and select option by index.
    Mirrors the logic in PenguinCreatorPage but is used inline here.
    """
    WebDriverWait(page.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[.//p[text()='{menu_text}']]"))
    ).click()

    options = WebDriverWait(page.driver, 10).until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "div[style*='opacity: 1'] > div.relative > button"
        ))
    )

    if index >= len(options):
        raise IndexError(f"{menu_text}: index {index} out of {len(options)} options.")

    options[index].click()

    WebDriverWait(page.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Volver')]"))
    ).click()

    time.sleep(0.5)

# Generate the pairwise combinations
keys, pairwise_combinations = generate_indexed_combinations(CATEGORY_COUNTS)

@pytest.mark.parametrize("combo_index", range(len(pairwise_combinations)))
def test_pairwise_penguin(driver, combo_index):
    """
    Generate penguins using pairwise combinations to ensure coverage across attribute pairs.
    Each combination applies a specific index from every attribute group.

    Additionally:
    - Log each generated penguin's image name and its combination to log.txt.
    """
    combo = pairwise_combinations[combo_index]
    page = PenguinCreatorPage(driver)
    page.load()
    time.sleep(2)

    # Select each feature using index from combination
    for category, index in zip(keys, combo):
        select_option_by_index(page, category, index)

    time.sleep(0.5)
    page.download_image()

    # Wait and rename using the helper (fix for default Chrome filename)
    image_name = f"pairwise_{combo_index+1}.png"
    wait_and_rename_image(
        old_name="pinguino.png",
        new_name=image_name,
        folder=PAIRWISE_DIR
    )

    # Write log entry: image name + combination details
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        combo_str = ", ".join(f"{category}: {index}" for category, index in zip(keys, combo))
        log.write(f"{image_name} -> {combo_str}\n")

    # Ensure the renamed image exists
    assert os.path.exists(os.path.join(PAIRWISE_DIR, image_name))
