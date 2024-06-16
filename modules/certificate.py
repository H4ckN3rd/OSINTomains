import ssl
import socket
from urllib.parse import urlparse

def get_ssl_certificate(domain):
    try:
        parsed_url = urlparse(domain)
        hostname = parsed_url.hostname
        port = parsed_url.port or 443

        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        if not cert:
            raise ValueError(f"No certificate presented by the server for {domain}")

        cert_info = {
            'subject': dict(x[0] for x in cert['subject']),
            'issuer': dict(x[0] for x in cert['issuer']),
            'version': cert['version'],
            'serialNumber': cert['serialNumber'],
            'notBefore': cert['notBefore'],
            'notAfter': cert['notAfter'],
            'subjectAltName': cert.get('subjectAltName', []),
            'OCSP': cert.get('OCSP', []),
            'caIssuers': cert.get('caIssuers', []),
        }
        
        return cert_info

    except Exception as e:
        print(f"Error fetching SSL certificate for {domain}: {e}")
        return None

if __name__ == "__main__":
    domain = input("Enter the Domain: ")
    ssl_cert = get_ssl_certificate(domain)
    if ssl_cert:
        print(f"SSL certificate for {domain}: {ssl_cert}")
    else:
        print("Failed to retrieve SSL certificate information.")
