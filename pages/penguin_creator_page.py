# pages/penguin_creator_page.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PenguinCreatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.tokovt.com/tu-pinguino"

    def load(self):
        self.driver.get(self.url)

    def open_size_menu(self):
        size_menu_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Tamaño']]"))
        )
        size_menu_btn.click()

    def select_size_by_index(self, index):
        # Esperar a que las opciones estén cargadas
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div[style*='opacity: 1'] > div.relative > button")
            )
        )
        buttons[index].click()

    def click_volver(self):
        volver_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Volver')]"))
        )
        volver_btn.click()

    def select_option_by_index(self, category_name, option_index):
        """
        Opens the category menu (by its visible name) and selects an option by index.
        This fixes the old bug where the function was using the wrong parameter for the menu name.
        """
        # Open the menu by category name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[.//p[text()='{category_name}']]"))
        ).click()

        # Select the option by index
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, "div[style*='opacity: 1'] > div.relative > button"
            ))
        )

        if option_index >= len(options):
            raise IndexError(f"{category_name}: index {option_index} out of {len(options)} options.")

        options[option_index].click()

        # Return to the main menu
        self.click_volver()

        time.sleep(0.5)

    def download_image(self):
        """
        Clicks the download button. 
        We no longer pass a filename here, Chrome will use the default 'pinguino.png'.
        """
        download_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Descargar')]"))
        )
        download_btn.click()
