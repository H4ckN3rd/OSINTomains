#whois.py
import whois

def get_domain_whois(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    whois_info = get_domain_whois(domain)
    print(whois_info)
