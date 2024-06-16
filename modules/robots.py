import requests
from urllib.parse import urlparse

def parse_robots_txt(content):
    lines = content.split('\n')
    rules = []

    for line in lines:
        line = line.strip()  

        # Match Allow or Disallow rules
        match = line.split(': ')
        if len(match) == 2 and match[0] in ['Allow', 'Disallow']:
            rule = {
                'label': match[0],
                'value': match[1]
            }
            rules.append(rule)

        # Match User-agent rules
        match = line.split(': ')
        if len(match) == 2 and match[0] == 'User-agent':
            rule = {
                'label': match[0],
                'value': match[1]
            }
            rules.append(rule)

    return {'robots': rules}

def fetch_robots_txt(url):
    try:
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

        response = requests.get(robots_url)

        if response.status_code == 200:
            parsed_data = parse_robots_txt(response.text)
            if not parsed_data['robots']:
                return {'skipped': 'No robots.txt file present, unable to continue'}
            return parsed_data
        else:
            return {
                'statusCode': response.status_code,
                'error': f"Failed to fetch robots.txt: {response.status_code}"
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': f"Error fetching robots.txt: {str(e)}"
        }
