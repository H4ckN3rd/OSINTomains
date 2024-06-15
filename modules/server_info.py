import requests

def get_server_location(domain):
    try:
        response = requests.get(f"https://ipinfo.io/{domain}/json")
        return response.json()
    except Exception as e:
        print(f"Error retrieving server location for {domain}: {e}")
        return None
