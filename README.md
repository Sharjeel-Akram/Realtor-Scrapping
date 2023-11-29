# Realtor.com Property Scraper

## Overview
This script is designed to scrape real estate listings from Realtor.com. It extracts information like title, price, location, and link for each listing and saves it into a CSV file. It uses BeautifulSoup for parsing HTML and the `fake_useragent` library to help with scraping.

## Requirements
- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `fake_useragent`
  - These can be installed via pip: `pip install requests beautifulsoup4 fake_useragent`

## Setup
1. Ensure Python 3.x is installed on your system.
2. Install the required libraries using the command: `pip install requests beautifulsoup4 fake_useragent`
3. Place the script in a desired directory.

## Usage
- Open a terminal or command prompt.
- Navigate to the directory containing the script.
- Run the script with the command: `python Realtor_Scrapping.py`
- The script will scrape data for predefined locations and save it in `Extracted_properties.csv`.

## Customization
To modify the locations for scraping, update the `locations` list in the script:
```python
locations = ['Location1', 'Location2', ...]
```
## Legal Considerations
- Web scraping activities are subject to legal and ethical considerations. It is crucial to comply with the terms of service and privacy policies of the website.
- Some websites explicitly prohibit scraping in their terms of service. Ensure that you review and understand Realtor.com's terms before scraping their site.
- This script is intended for educational purposes. Use it responsibly and ethically. Do not use it to access or collect data in a manner that violates laws or regulations.
- Be aware of data privacy laws and regulations that apply to publicly scraped data, especially if it involves personal information.

