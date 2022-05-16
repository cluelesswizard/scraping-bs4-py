import requests, json
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
totalScrapedInfo = []

links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    totalScrapedInfo.append(anchor.text) # Display the innerText of each anchor

file = open('movies.json', mode='w', encoding='utf-8')
file.write(json.dumps(totalScrapedInfo))