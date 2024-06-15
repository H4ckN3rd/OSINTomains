import whois

def get_domain_whois(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None
