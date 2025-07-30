# 🐧 Penguin Creator Visual Testing - TokoVT

This project uses **Selenium** with the **Page Object Model (POM)** design pattern and **Pytest** to test the penguin customization tool on [https://www.tokovt.com/tu-pinguino](https://www.tokovt.com/tu-pinguino).

## 📦 What does it do?

- Automates penguin creation with different customization combinations
- Uses the **Pairwise (AllPairs) testing technique** to minimize the total number of combinations while ensuring full pair coverage across categories
- Downloads the generated image for each test combination
- Renames and organizes the images in `/images/pairwise_test/`
- Logs each generated image and its selected attributes in `log.txt`
- Compares image hashes (optional) to ensure visual uniqueness

---

## 🧱 Project Structure

```
penguin_tester/
├── pages/                         # Page Object classes
│   └── penguin_creator_page.py
├── tests/                         # Test cases
│   ├── test_pairwise_penguins.py
│   ├── test_download.py
│   └── test_size_options.py
├── utils/                         # Utilities
│   ├── pairwise_generator.py      # Pairwise (AllPairs) generator
│   ├── image_utils.py             # Download renaming and helpers
│   ├── image_hash_checker.py
│   └── clean_images.py
├── images/                        # Downloaded image output
│   └── pairwise_test/             # Pairwise test results
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

### 3. Run all pairwise penguin tests:
```bash
pytest tests/test_pairwise_penguins.py
```

### 4. Check hash comparison manually (optional):
```python
from utils.image_hash_checker import all_image_hashes_unique

print(all_image_hashes_unique("images/pairwise_test"))
```

---

## 🔍 How it works

### Pairwise Testing (AllPairs)
- When testing multiple categories (Size, Colors, Eyes, Accessories, etc.), running the **full Cartesian product** of all options would produce an exponentially large number of tests.
- This project uses the `allpairspy` library to generate a **reduced set of combinations**:
  - Every possible *pair of values* across categories is tested at least once.
  - The number of tests is drastically reduced while still achieving strong coverage.

**Example:**
- Categories:  
  - Size: 3 options  
  - Color: 10 options  
  - Eyes: 15 options  
- Full Cartesian product: **3 × 10 × 15 = 450 combinations**  
- Pairwise (AllPairs): ~30–50 combinations  
  - All pairs `(Size, Color)`, `(Size, Eyes)`, `(Color, Eyes)` will appear at least once.

### Test Flow
1. Load the Penguin Creator page.
2. For each pairwise combination:
   - Select one option per category (e.g., Size=1, Color=5, Eyes=3).
   - Click "Volver" to return to the main view.
   - Click "Descargar" and download the penguin image.
   - Rename the image to `pairwise_{index}.png` using the helper.
   - Log the filename and selected options to `log.txt`.
3. Optionally validate that all generated images are visually unique using perceptual hashing.

---

## 🧼 Extra: Clear all images
To remove all files in `/images/`:

```bash
python utils/clean_images.py
```

---

Created with 💻 by Roberto using Python, Selenium, and 🐧. Now with **Pairwise Testing (AllPairs)** for efficient and scalable coverage!
