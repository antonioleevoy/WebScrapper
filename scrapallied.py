import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to scrape the website and extract part number and manufacturer name
def scrape_website(part_number, driver):
    url = f"https://us.rs-online.com/product/{part_number}"
    driver.get(url)

    # Wait for the page to load and find the manufacturer name
    manufacturer_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "brand-name"))
    )
    manufacturer = manufacturer_element.text.strip() if manufacturer_element else "Not Found"

    return manufacturer

# Read part numbers from CSV and scrape the website
def scrape_csv(input_file, output_file):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    service = Service('C:/Users/leevo/OneDrive/Documents/scrapper/chromedriver.exe')  # Provide the path to your ChromeDriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    with open(input_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = list(reader)

    results = []
    for row in data:
        part_number = row[0]
        manufacturer = scrape_website(part_number, driver)
        results.append([part_number, manufacturer])

    driver.quit()

    # Write results to output CSV
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Part Number", "Manufacturer"])
        writer.writerows(results)

    print(f"Scraping completed. Results saved to {output_file}.")

# Usage
input_csv_file = "C:/Users/leevo/OneDrive/Documents/scrapper/part_numbers.csv"
output_csv_file = "C:/Users/leevo/OneDrive/Documents/scrapper/scraped_data.csv"
scrape_csv(input_csv_file, output_csv_file)
