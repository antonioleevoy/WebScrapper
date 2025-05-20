import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_manufacturer(part_number):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode

    service = Service('C:/Users/leevo/OneDrive/Documents/scrapper/chromedriver.exe')  # Replace with the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://uk.rs-online.com/web/c/?sra=oss&r=t&searchTerm={part_number}"
    driver.get(url)

    brand_element = brand_element.find_element(By.CLASS_NAME, 'vendor-name')

    return brand_element

    if brand_element:
        manufacturer = brand_element.text.strip()
        driver.quit()
        return manufacturer
    driver.quit()
    return "None"

def export_to_csv(data):
    with open('C:/Users/leevo/OneDrive/Documents/scrapper/manufacturer_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Part Number', 'Manufacturer'])
        for part_number, manufacturer in data.items():
            writer.writerow([part_number, manufacturer])

def read_part_numbers_from_csv(file_path):
    part_numbers = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            part_number = row[0].strip()
            part_numbers.append(part_number)
    return part_numbers

input_csv_file = 'C:/Users/leevo/OneDrive/Documents/scrapper/part_numbers.csv'  # Replace with the path to your input CSV file
part_numbers = read_part_numbers_from_csv(input_csv_file)

data = {}
for part_number in part_numbers:
    manufacturer = scrape_manufacturer(part_number)
    data[part_number] = manufacturer

export_to_csv(data)

print("Data exported to manufacturer_data.csv file.")
