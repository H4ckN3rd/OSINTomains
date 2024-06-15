from Wappalyzer import Wappalyzer, WebPage
import requests

def get_tech_stack(domain):
    try:
        # Ensure the domain has the correct protocol prefix
        if not domain.startswith('http://') and not domain.startswith('https://'):
            url = f'https://{domain}'
        else:
            url = domain

        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        webpage = WebPage.new_from_content(response.content, url)

        # Analyze the technologies using Wappalyzer
        wappalyzer = Wappalyzer.latest()
        technologies = wappalyzer.analyze(webpage)

        return technologies

    except Exception as e:
        print(f"Error retrieving tech stack for {domain}: {e}")
        return None
