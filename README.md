
# Part Number Scraper

This Python script scrapes manufacturer information from the manufacturer websites for a list of part numbers provided in a CSV file.

## 📌 Features

- Automatically navigates to the RS product page using Selenium.
- Extracts the manufacturer name and a link to the manufacturer’s page.
- Writes the results to a CSV file (`scraped_data.csv`).
- Runs headlessly (no browser window pops up).

## 🧰 Requirements

- Python 3.x
- Google Chrome installed
- ChromeDriver (compatible with your Chrome version)
- Required Python packages:
  - `selenium`

## 📂 File Structure

```
scrapper/
├── chromedriver.exe
├── part_numbers.csv         # Input file (with header and part numbers)
├── scraped_data.csv         # Output file (automatically created)
└── scraper_script.py        # The main script
```

## 📄 Input CSV Format

Your `part_numbers.csv` should look like this:

```
Part Number
123456
789012
...
```

## 🚀 How to Use

1. **Install Selenium**:
   ```bash
   pip install selenium
   ```

2. **Download ChromeDriver**:
   - Get the version that matches your Chrome from: https://sites.google.com/chromium.org/driver/
   - Place it in your desired location and update the path in the script:
     ```python
     chrome_driver_path = 'C:/Users/leevo/Documents/scrapper/chromedriver.exe'
     ```

3. **Update Input File**:
   - Add your part numbers to `part_numbers.csv`.

4. **Run the Script**:
   ```bash
   python scrapper.py
   ```

5. **Check Output**:
   - The scraped data will be saved in `scraped_data.csv` with the following columns:
     - `Part Number`
     - `Manufacturer`
     - `Manufacturer Link`

## 🛠 Notes

- The script uses explicit waits (`WebDriverWait`) to ensure that the manufacturer element is loaded before attempting to scrape.
- This scraper assumes a consistent page layout on the RS website. If RS changes their structure, the script may need updating.

## 📃 License

This project is for educational and personal use only. Be sure to review RS Components' [terms of service](https://us.rs-online.com/) before scraping their website.
