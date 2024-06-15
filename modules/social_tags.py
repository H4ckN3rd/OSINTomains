import requests
from bs4 import BeautifulSoup

def get_social_tags(domain):
    try:
        response = requests.get(domain)
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = {
            'og:title': soup.find('meta', property='og:title'),
            'og:description': soup.find('meta', property='og:description'),
            'twitter:title': soup.find('meta', name='twitter:title'),
            'twitter:description': soup.find('meta', name='twitter:description'),
        }
        return {k: v['content'] if v else None for k, v in tags.items()}
    except Exception as e:
        print(f"Error retrieving social tags for {domain}: {e}")
        return None
