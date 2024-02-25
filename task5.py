#Web Scraping using BeautifulSoup Library:
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find specific elements on the page
    # For example, find all <a> tags (links) and print their href attribute
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # Find specific elements with a class name
    # For example, find all elements with class 'title' and print their text
    titles = soup.find_all(class_='title')
    for title in titles:
        print(title.text)

    # Find specific elements with an id
    # For example, find the element with id 'header' and print its text
    header = soup.find(id='header')
    if header:
        print(header.text)
else:
    print('Failed to retrieve the webpage.')
