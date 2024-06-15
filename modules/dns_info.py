import dns.resolver

def get_dns_records(domain):
    try:
        records = dns.resolver.resolve(domain, 'A')
        return [str(record) for record in records]
    except Exception as e:
        return None
