import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
import time
import random

def scrape_Realtor(location):
    ua = UserAgent()
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Encoding':'identity'}
    header = {'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) {str(ua.chrome)}', 'Accept-Encoding':'identity'}
    time.sleep(random.uniform(2, 5))
    base_url = f"https://www.realtor.com/realestateandhomes-search/{location}"
    
    print("Scrapping has been Started.............")
    with open('Extracted_properties.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Title', 'Price', 'Location', 'Link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        page = 1
        while True:
            url = f"{base_url}/pg-{page}"
            try:
                response = requests.get(url, headers=header)
                if response.status_code != 200:
                    print(f"Failed and Status Code: {response.status_code}")
                    print(f"Response: {response.text[:500]}")
                    break

                soup = BeautifulSoup(response.content, 'lxml')
                for item in soup.select('.BasePropertyCard_propertyCardWrap__Z5y4p'):
                    try:
                        title = item.select_one('[data-testid=broker-title]')
                        price = item.select_one('[data-testid=card-price]')
                        address1 = item.select_one('[data-testid=card-address-1]')
                        address2 = item.select_one('[data-testid=card-address-2]')
                        listing_url = item.select_one('a', {'class': 'LinkComponent_anchor__0C2xC'})['href']
                        if title and price and address1 and address2 and listing_url:
                            title_text = title.get_text()
                            price_text = price.get_text()
                            location_text = f"{address1.get_text()}, {address2.get_text()}"
                            if not listing_url.startswith('http'):
                                listing_url = 'https://www.zillow.com' + listing_url
                            writer.writerow({'Title': title_text, 'Price': price_text, 'Location': location_text, 'Link': listing_url})
                    except Exception as e:
                        pass
                next_link = soup.find('a', class_='next-link')
                if next_link:
                    page += 1
                else:
                    break
                time.sleep(2)
            except Exception as e:
                print(f"An error occurred: {str(e)}")
    print("Scraping completed. Data saved to 'Extracted_properties.csv'.")
locations = ['Washington','San-Francisco_CA', ]
for i in locations:
    scrape_Realtor(i)