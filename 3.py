import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty list to hold quote data
all_quotes = []

page = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        all_quotes.append({
            "Quote": text,
            "Author": author,
            "Tags": ', '.join(tags)
        })

    page += 1

# Create DataFrame and save to CSV
df = pd.DataFrame(all_quotes)
df.to_csv("quotes.csv", index=False)

print("✅ All quotes saved to 'quotes.csv'")
