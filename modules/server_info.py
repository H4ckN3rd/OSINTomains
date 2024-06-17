import requests

def get_server_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json', timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error retrieving server location for {ip}: {e}")
        return {'error': str(e), 'city': 'Unknown', 'region': 'Unknown', 'country': 'Unknown'}
    

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    whois_info = get_server_location(domain)
    print(whois_info)
