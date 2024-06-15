import requests

def get_headers(domain):
    try:
        response = requests.get(domain)
        return response.headers
    except Exception as e:
        print(f"Error retrieving headers for {domain}: {e}")
        return None
