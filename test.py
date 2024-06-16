import requests
import zipfile
import csv
import os
from urllib.parse import urlparse

# Should also work with the following sources:
#https://www.domcop.com/files/top/top10milliondomains.csv.zip
# https://tranco-list.eu/top-1m.csv.zip
# https://www.domcop.com/files/top/top10milliondomains.csv.zip
# https://radar.cloudflare.com/charts/LargerTopDomainsTable/attachment?id=525&top=1000000
# https://statvoo.com/dl/top-1million-sites.csv.zip

FILE_URL = 'top-1m.csv'
TEMP_FILE_PATH = 'top-1m.csv'

def handler(url):
    try:
        domain = urlparse(url).hostname
        if not domain:
            raise ValueError('Invalid URL')

        # Download and unzip the file if not in cache
        if not os.path.exists(TEMP_FILE_PATH):
            response = requests.get(FILE_URL, stream=True)
            with open('/tmp/top-1m.csv.zip', 'wb') as f:
                f.write(response.content)
            with zipfile.ZipFile('/tmp/top-1m.csv.zip', 'r') as zip_ref:
                zip_ref.extractall('/tmp')

        # Parse the CSV and find the rank
        with open(TEMP_FILE_PATH, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=['rank', 'domain'])
            for row in csv_reader:
                if row['domain'] == domain:
                    return {
                        'domain': domain,
                        'rank': row['rank'],
                        'isFound': True,
                    }
        
        return {
            'skipped': f"Skipping, as {domain} is not present in the Umbrella top 1M list.",
            'domain': domain,
            'isFound': False,
        }

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    domain = input("Enter the Domain: ")
    result = handler(domain)
    print(result)
