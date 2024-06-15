import requests

def get_cookies(domain):
    try:
        response = requests.get(domain)
        return response.cookies
    except Exception as e:
        print(f"Error retrieving cookies for {domain}: {e}")
        return None
