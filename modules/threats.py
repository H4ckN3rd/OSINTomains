import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_google_safe_browsing_result(url):
    try:
        api_key = os.getenv('GOOGLE_CLOUD_API_KEY')
        if not api_key:
            raise ValueError('GOOGLE_CLOUD_API_KEY is not set in environment variables.')

        api_endpoint = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
        threat_info = {
            'threatInfo': {
                'threatTypes': [
                    'MALWARE', 'SOCIAL_ENGINEERING', 'UNWANTED_SOFTWARE',
                    'POTENTIALLY_HARMFUL_APPLICATION', 'API_ABUSE'
                ],
                'platformTypes': ['ANY_PLATFORM'],
                'threatEntryTypes': ['URL'],
                'threatEntries': [{'url': url}]
            }
        }

        response = requests.post(api_endpoint, json=threat_info)
        response_data = response.json()

        if 'matches' in response_data:
            return {'unsafe': True, 'details': response_data['matches']}
        else:
            return {'unsafe': False}

    except Exception as e:
        return {'error': f'Request to Google Safe Browsing failed: {str(e)}'}

def get_cloudmersive_result(url):
    try:
        api_key = os.getenv('CLOUDMERSIVE_API_KEY')
        if not api_key:
            raise ValueError('CLOUDMERSIVE_API_KEY is not set in environment variables.')

        endpoint = 'https://api.cloudmersive.com/virus/scan/website'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Apikey': api_key
        }
        data = {'Url': url}

        response = requests.post(endpoint, data=data, headers=headers)
        return response.json()

    except Exception as e:
        return {'error': f'Request to Cloudmersive failed: {str(e)}'}

def handler(url):
    try:
        google_safe_browsing = get_google_safe_browsing_result(url)
        cloudmersive = get_cloudmersive_result(url)

        result = {
            'google_safe_browsing': google_safe_browsing,
            'cloudmersive': cloudmersive
        }

        return result

    except Exception as e:
        return {'error': f'Handler function error: {str(e)}'}

# Example usage if module is run directly
if __name__ == '__main__':
    test_url = input("Enter the URL: ")
    try:
        metrics = handler(test_url)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")
