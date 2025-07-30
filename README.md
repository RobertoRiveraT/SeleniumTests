# 🐧 Penguin Creator Visual Testing - TokoVT

This project uses **Selenium** with the **Page Object Model (POM)** design pattern and **Pytest** to test the penguin customization tool on [https://www.tokovt.com/tu-pinguino](https://www.tokovt.com/tu-pinguino).

## 📦 What does it do?

- Automates penguin creation with different body sizes
- Downloads the generated image
- Renames and organizes the images in `/images/size_test/`
- Compares image hashes to ensure that each body size results in a visually different penguin

---

## 🧱 Project Structure

```
penguin_tester/
├── pages/                         # Page Object classes
│   └── penguin_creator_page.py
├── tests/                         # Test cases
│   ├── test_download.py
│   └── test_size_options.py
├── utils/                         # Utilities
│   ├── image_utils.py
│   ├── image_hash_checker.py
│   └── clean_images.py
├── images/                        # Downloaded image output
│   └── size_test/
├── conftest.py                    # Pytest fixtures
└── requirements.txt
```

---

## 🚀 How to run

### 1. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Clean old images (optional):
```bash
python utils/clean_images.py
```

### 3. Run all penguin size tests:
```bash
pytest tests/test_size_options.py
```

### 4. Check hash comparison manually (optional):
```python
from utils.image_hash_checker import all_image_hashes_unique

print(all_image_hashes_unique("images/size_test"))
```

---

## 🔍 How it works

- The test selects one of the 3 penguin body sizes
- After selecting a size, it clicks "Volver" to return to the main view
- It then clicks "Descargar" and renames the resulting image (e.g., `pinguino_size_1.png`)
- After all sizes are tested, the test verifies that all 3 images are visually different using perceptual hashing

---

## 🧼 Extra: Clear all images
To remove all files in `/images/`:

```bash
python utils/clean_images.py
```

---

## ✨ Next ideas

- Automate testing of other customization categories (e.g. accessories, hats)
- Validate image differences across full penguin configurations
- Integrate screenshot comparison or visual diffs with OpenCV

---

Created with 💻 by Roberto using Python, Selenium, and 🐧.