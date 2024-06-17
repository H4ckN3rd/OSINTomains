import requests
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

def fetch_sitemap(domain):
    sitemap_url = domain.rstrip('/') + '/sitemap.xml?'
    hard_timeout = 5

    try:
        # Try to fetch sitemap directly
        try:
            sitemap_res = requests.get(sitemap_url, timeout=hard_timeout)
            sitemap_res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                robots_url = domain.rstrip('/') + '/robots.txt'
                robots_res = requests.get(robots_url, timeout=hard_timeout)
                robots_txt = robots_res.text.split('\n')

                for line in robots_txt:
                    if line.lower().startswith('sitemap:'):
                        sitemap_url = line.split(':', 1)[1].strip()
                        break

                if not sitemap_url:
                    return {'skipped': 'No sitemap found'}

                sitemap_res = requests.get(sitemap_url, timeout=hard_timeout)
            else:
                raise e

        # Check if the response is valid XML
        try:
            root = ET.fromstring(sitemap_res.content)
        except ET.ParseError:
            return {'error': 'Invalid XML content'}

        # Extract URLs from sitemap
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        sitemap_urls = [elem.text.strip() for elem in root.findall('.//ns:loc', namespace)]

        return {'sitemap_urls': sitemap_urls}

    except requests.exceptions.Timeout:
        return {'error': f'Request timed out after {hard_timeout} seconds'}

    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == "__main__":
    test_domain = input("Enter the domain: ")  
    try:
        metrics = fetch_sitemap(test_domain)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")
