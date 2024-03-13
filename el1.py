import requests
from bs4 import BeautifulSoup
import json
import os
import argparse

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
def download_images_and_save_json(base_url, start_number, end_number, output_file):
    data = {}
    for i in range(start_number, end_number + 1):
        url = f"{base_url}/{i}"
        html_content = download_html(url)
        image_urls = parse_html(html_content)
        data[f'{i}'] = image_urls

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images from URL and save to JSON.')
    parser.add_argument('--url', type=str, help='URL to download images from')
    parser.add_argument('--start', type=int, default=1, help='Starting number for image URLs (default: 1)')
    parser.add_argument('--end', type=int, default=58, help='Ending number for image URLs (default: 58)')
    parser.add_argument('--output', type=str, help='Output JSON file name')

    args = parser.parse_args()

    if args.url and args.output:
        base_url = args.url
        start_number = args.start
        end_number = args.end
        download_images_and_save_json(base_url, start_number, end_number, args.output)
    else:
        print("Please provide both --url and --output arguments.")
