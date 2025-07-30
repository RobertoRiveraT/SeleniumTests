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

    def download_image(self):
        download_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Descargar')]"))
        )
        download_btn.click()

    def click_volver(self):
        volver_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Volver')]"))
        )
        volver_btn.click()
