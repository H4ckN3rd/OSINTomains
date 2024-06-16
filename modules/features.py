from Wappalyzer import Wappalyzer, WebPage
import requests
from urllib.parse import urlparse

class WappalyzerError(Exception):
    pass

def fetch_tech_stack(url):
    # Ensure the URL is properly formatted
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = f'http://{url}'

    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze(webpage)
        return technologies
    except Exception as e:
        raise WappalyzerError(f"Error analyzing tech stack: {e}")

def middleware(handler):
    def wrapper(url, *args, **kwargs):
        try:
            return handler(url, *args, **kwargs)
        except Exception as e:
            return {'error': str(e)}
    return wrapper

@middleware
def handler(url):
    return fetch_tech_stack(url)

# Example usage:
if __name__ == "__main__":
    url = input("Enter the URL: ")
    result = handler(url)
    print(result)
