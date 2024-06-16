import dns.resolver
import dns.reversename
import requests

def resolve_dns(domain):
    try:
        domain = domain.replace("http://", "").replace("https://", "")
        addresses = dns.resolver.resolve(domain, 'A')
        results = []

        for ipval in addresses:
            address = ipval.to_text()
            try:
                hostname = dns.reversename.from_address(address)
                reversed_names = dns.resolver.resolve(hostname, 'PTR')
                hostname = str(reversed_names[0])
            except Exception:
                hostname = None
            
            try:
                doh_response = requests.get(f'https://{address}/dns-query')
                doh_direct_supports = doh_response.status_code == 200
            except requests.RequestException:
                doh_direct_supports = False

            results.append({
                'address': address,
                'hostname': hostname,
                'dohDirectSupports': doh_direct_supports,
            })

        return {
            'domain': domain,
            'dns': results,
        }

    except Exception as e:
        raise Exception(f"An error occurred while resolving DNS: {e}")

if __name__ == "__main__":
    domain = input("Enter the Domain: ")
    dns_info = resolve_dns(domain)
    if dns_info:
        print(f"DNS info for {domain}: {dns_info}")
    else:
        print("Failed to retrieve DNS information.")
