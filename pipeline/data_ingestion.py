import requests
from bs4 import BeautifulSoup
import json

def scrape_data_from_web(url):
    """
    Scrapes data from the given website URL.
    Returns the text content of the page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract page content (you can customize this for specific tags)
    page_content = soup.get_text()
    return page_content

def collect_data_from_api(api_url):
    """
    Collects data from the specified API endpoint.
    Returns JSON data.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}")

def save_ingested_data_to_file(content, filename):
    """
    Saves ingested data (raw) to a local file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Data saved to {filename}")

def ingest_data_via_api(file_path):
    """
    Sends ingested data to Sharanya's FastAPI endpoint for ingestion.
    """
    files = {'file': open(file_path, 'rb')}
    response = requests.post('http://localhost:8000/ingest', files=files)  # Adjust URL if needed
    if response.status_code == 200:
        print("File successfully ingested via API.")
    else:
        print(f"Failed to ingest file. Status code: {response.status_code}")

# Example usage:
if __name__ == "__main__":
    url = "https://example.com/article"
    api_url = "https://api.example.com/data"

    # Scrape from web
    content = scrape_data_from_web(url)
    save_ingested_data_to_file(content, 'web_data.txt')

    # Collect from API
    api_data = collect_data_from_api(api_url)
    save_ingested_data_to_file(json.dumps(api_data), 'api_data.json')

    # Ingest the web data file via API
    ingest_data_via_api('web_data.txt')

    # Ingest the API data file via API
    ingest_data_via_api('api_data.json')
