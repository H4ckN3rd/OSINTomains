import requests

def get_carbon_footprint(domain):
    try:
        response = requests.get(f"https://api.websitecarbon.com/site?url={domain}")
        return response.json()
    except Exception as e:
        return str(e)
