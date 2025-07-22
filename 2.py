import requests
from bs4 import BeautifulSoup

page = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    # Break if the page doesn't exist
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break

    print(f"\n--- Page {page} ---\n")
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"{text} — {author}")

    page += 1  # move to next page
