from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ---- ✅ CORRECTED DRIVER PATH ----
CHROME_DRIVER_PATH = r"D:\Download_D\38833FF26BA1D.UnigramPreview_g9c9v27vpyspw!App\chromedriver-win64\chromedriver.exe"
OUTPUT_FILE = "sector_coordinates.csv"
HEADLESS = True  # Set to False if you want to see browser popup

# ---- SETUP ----
options = Options()
if HEADLESS:
    options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--log-level=3")

# ✅ Create Service object
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# ---- FUNCTION TO FETCH COORDINATES ----
def get_coordinates(sector):
    try:
        search_term = f"sector {sector} gurgaon latitude and longitude"
        url = f"https://www.google.com/search?q={search_term}"
        driver.get(url)

        wait = WebDriverWait(driver, 5)
        coord_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wvKXQ")))
        return coord_div.text.strip()

    except (TimeoutException, NoSuchElementException):
        return None

# ---- MAIN LOOP ----
data = []

for sector in range(1, 116):
    print(f"Fetching Sector {sector}...", end=" ")
    coords = get_coordinates(sector)
    if coords:
        print(f"✅ {coords}")
    else:
        print("❌ Not found")
    data.append({"Sector": f"Sector {sector}", "Coordinates": coords})
    time.sleep(1.5)  # polite delay

# ---- SAVE TO CSV ----
df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Saved all coordinates to '{OUTPUT_FILE}'")

# ---- CLOSE BROWSER ----
driver.quit()
