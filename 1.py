import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quote containers
quotes = soup.find_all('div', class_='quote')

# Step 4: Loop through each quote and print text + author
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f"{text} — {author}")
