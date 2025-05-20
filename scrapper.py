import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_website(part_number):
    options = Options()
    options.add_argument("--headless")

    chrome_driver_path = 'C:/Users/leevo/OneDrive/Documents/scrapper/chromedriver.exe'

    service = Service(chrome_driver_path)
    service.start()

    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://us.rs-online.com/product/{part_number}/?keyword={part_number}"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    manufacturer_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'manufacturer')))

    part_info = {
        'Part Number': part_number,
        'Manufacturer': 'N/A',
        'Manufacturer Link': 'N/A'
    }

    manufacturer_link = manufacturer_element.find_element(By.TAG_NAME, 'a')
    if manufacturer_link:
        manufacturer_name = manufacturer_link.text.strip()
        manufacturer_href = manufacturer_link.get_attribute('href')
        part_info['Manufacturer'] = manufacturer_name
        part_info['Manufacturer Link'] = manufacturer_href

    driver.quit()

    return part_info


def main():
    with open('C:/Users/leevo/OneDrive/Documents/scrapper/part_numbers.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        part_numbers = [row[0] for row in reader]

    scraped_data = []
    for part_number in part_numbers:
        part_info = scrape_website(part_number)
        scraped_data.append(part_info)

    with open('C:/Users/leevo/OneDrive/Documents/scrapper/scraped_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Part Number', 'Manufacturer', 'Manufacturer Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scraped_data)

    print('Scraping complete. Data saved to scraped_data.csv.')


if __name__ == '__main__':
    main()
