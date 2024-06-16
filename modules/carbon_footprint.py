import requests

def get_carbon_footprint(domain):
    try:
        response = requests.get(f"https://api.websitecarbon.com/site?url={domain}")
        return response.json()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    test_url = input("Enter the URL: ")  # Replace with the URL you want to analyze
    try:
        metrics = get_carbon_footprint(test_url)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")
