import requests
from bs4 import BeautifulSoup

# Specify the URL you want to scrape
url = 'https://microsoft.com'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract titles (assuming titles are in <h1> or <h2> tags)
    titles = soup.find_all(['h1', 'h2'])
    for title in titles:
        print(f"Title: {title.text}")

    # Extract subtitles (adjust the tag accordingly)
    subtitles = soup.find_all('h3')
    for subtitle in subtitles:
        print(f"Subtitle: {subtitle.text}")

    # Extract paragraphs (assuming paragraphs are in <p> tags)
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(f"Paragraph: {paragraph.text}")

    # Extract captions (adjust the tag accordingly)
    captions = soup.find_all('span', class_='caption')
    for caption in captions:
        print(f"Caption: {caption.text}")

else:
    print(f"Error: {response.status_code}")
