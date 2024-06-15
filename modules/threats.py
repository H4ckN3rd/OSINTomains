import requests
import logging

def get_threats(domain):
    try:
        url = f"https://some-threat-api.com/{domain}"
        response = requests.get(url)
        data = response.json()
        
        if 'detected_urls' in data:
            threats = data['detected_urls']
        else:
            logging.warning(f"No 'detected_urls' key found in response for {domain}")
            threats = []
        
        return threats
    except Exception as e:
        logging.error(f"Error retrieving threats for {domain}: {e}")
        return None
