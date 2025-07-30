import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.penguin_creator_page import PenguinCreatorPage
from utils.pairwise_generator import generate_combinations

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # o elimina esto para ver el navegador
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("color, hat, accessory", generate_combinations())
def test_penguin_combination(driver, color, hat, accessory):
    page = PenguinCreatorPage(driver)
    page.load()

    page.select_color(color)
    page.select_hat(hat)
    page.select_accessory(accessory)

    assert page.penguin_preview_loaded()
