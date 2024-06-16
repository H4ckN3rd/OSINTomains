import requests

def check_security_headers(domain):
    if not domain.startswith('http'):
        domain = f'http://{domain}'

    try:
        response = requests.get(domain)
        headers = response.headers
        return {
            'strictTransportPolicy': 'strict-transport-security' in headers,
            'xFrameOptions': 'x-frame-options' in headers,
            'xContentTypeOptions': 'x-content-type-options' in headers,
            'xXSSProtection': 'x-xss-protection' in headers,
            'contentSecurityPolicy': 'content-security-policy' in headers,
        }
    except Exception as error:
        return {
            'statusCode': 500,
            'error': str(error),
        }

if __name__ == "__main__":
    test_domain = input("Enter the domain: ")  
    try:
        metrics = check_security_headers(test_domain)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")