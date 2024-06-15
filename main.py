import os
import time
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader
from modules.certificate import get_ssl_certificate
from modules.dns_info import get_dns_records
from modules.domain_info import get_domain_whois
from modules.headers import get_headers
from modules.server_info import get_server_location
from modules.cookies import get_cookies
from modules.social_tags import get_social_tags
from modules.threats import get_threats
from modules.global_ranking import get_global_ranking
from modules.nmap import run_nmap
from modules.carbon_footprint import get_carbon_footprint
from modules.tech_stack import get_tech_stack  # Import your function here
from modules.quality import get_quality_metrics
import socket

def resolve_domain_to_ip(domain, retries=3, delay=2):
    parsed_url = urlparse(domain)
    domain = parsed_url.netloc or parsed_url.path

    for i in range(retries):
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror as e:
            if i < retries - 1:
                print(f"Attempt {i+1}/{retries} failed to resolve {domain}: {e}")
                time.sleep(delay)
            else:
                raise e

def create_html_report(data):
    template_dir = os.path.abspath('templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('report_template.html')
    output = template.render(data=data)
    with open('report.html', 'w') as f:
        f.write(output)

def main(domain):
    if not domain.startswith('https://'):
        domain = 'https://' + domain
    
    try:
        ip_address = resolve_domain_to_ip(domain)
        if ip_address:
            print(f"IP address: {ip_address}")

            data = {
                'domain': domain,
                'ip_address': ip_address,
                'server_location': get_server_location(ip_address),  # Use IP address here
                'ssl_certificate': get_ssl_certificate(domain),
                'whois': get_domain_whois(domain),
                'dns_records': get_dns_records(domain),
                'headers': get_headers(domain),
                'server_info': get_server_location(domain),
                'cookies': get_cookies(domain),
                'social_tags': get_social_tags(domain),
                'global_ranking': get_global_ranking(domain),
                'open_ports': run_nmap(ip_address),  # Use IP address for Nmap
                'carbon_footprint': get_carbon_footprint(domain),
                'tech_stack': get_tech_stack(domain),
                'quality_metrics': get_quality_metrics(domain),
            }

            # Print data for debugging purposes
            for key, value in data.items():
                print(f"{key}: {value}")

            create_html_report(data)
            print("Report generated: report.html")

        else:
            print(f"Failed to resolve domain {domain}. No IP address found.")

    except socket.gaierror as e:
        print(f"Failed to resolve domain: {e}")

if __name__ == "__main__":
    domain = input("Enter the Domain:")  # Replace with the domain you want to analyze
    main(domain)
