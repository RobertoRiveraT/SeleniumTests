# conftest.py

import os
import shutil
import pytest
from utils.image_utils import DOWNLOAD_DIR

@pytest.fixture(scope="session", autouse=True)
def setup_download_folder():
    # Esto se ejecuta UNA SOLA VEZ antes de todos los tests
    if os.path.exists(DOWNLOAD_DIR):
        shutil.rmtree(DOWNLOAD_DIR)
    os.makedirs(DOWNLOAD_DIR)
