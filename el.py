import requests
from bs4 import BeautifulSoup
import json
import os

# Function to download HTML content from a URL
def download_html(url):
    response = requests.get(url)
    return response.text

# Function to parse HTML and extract image URLs
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    figure_tags = soup.find_all('figure', class_='m-0')
    image_urls = [figure.find('img')['src'] for figure in figure_tags]
    return image_urls

# Function to download images and save to JSON
def download_images_and_save_json(base_url, start_number, end_number):
    data = {}
    for i in range(start_number, end_number + 1):
        url = f"{base_url}/{i}"
        html_content = download_html(url)
        image_urls = parse_html(html_content)
        data[f'{i}'] = image_urls

    with open('image_urls.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Main function
if __name__ == "__main__":
    base_url = 'https://uniform.wingzero.tw/school/photos/twes'
    start_number = 1
    end_number = 58
    download_images_and_save_json(base_url, start_number, end_number)
