import requests
from bs4 import BeautifulSoup
import os

# Specify the base URL and file count
base_url = 'https://en.wikipedia.org/wiki/Wikipedia:About'
file_count = 1

# Function to save text data to a text file
def save_to_text(title, subtitle, paragraphs, captions):
    global file_count
    file_name = f"output_{file_count}.txt"

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n\n")

        if subtitle:
            file.write(f"Subtitle: {subtitle}\n\n")

        for paragraph in paragraphs:
            file.write(f"Paragraph: {paragraph}\n")

        for caption in captions:
            file.write(f"Caption: {caption}\n")

    print(f"Data saved to {file_name}")
    file_count += 1

# Send an HTTP request to the URL
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract titles, subtitles, paragraphs, and captions
    titles = [title.text for title in soup.find_all(['h1', 'h2'])]
    subtitles = [subtitle.text for subtitle in soup.find_all('h3')]
    paragraphs = [paragraph.text for paragraph in soup.find_all('p')]
    captions = [caption.text for caption in soup.find_all('span', class_='caption')]

    # Save data to a text file
    if titles:
        title = titles[0]  # Assuming there is only one title
    else:
        title = "Untitled"

    subtitle = subtitles[0] if subtitles else None  # Assuming there is only one subtitle

    save_to_text(title, subtitle, paragraphs, captions)

else:
    print(f"Error: {response.status_code}")
