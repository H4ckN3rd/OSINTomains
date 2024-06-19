import os
import time
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader
from modules.certificate import get_ssl_certificate
from modules.carbon_footprint import get_carbon_footprint
from modules.cookies import get_cookies
from modules.dns_info import resolve_dns
from modules.domain_info import get_domain_whois
from modules.firewall import detect_waf
#from modules.global_ranking import get_global_ranking
from modules.headers import get_headers
from modules.nmap import run_nmap
from modules.quality import get_quality_metrics
from modules.robots import fetch_robots_txt
from modules.sec_headers import check_security_headers
from modules.server_info import get_server_location
from modules.sitemap import fetch_sitemap
from modules.social_tags import get_social_tags
from modules.threats import handler
from modules.tech_stack import get_tech_stack 
import socket

def print_ascii_art():
    art = r"""
#   $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\                                $$\                     
#  $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|                               \__|                    
#  $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\ $$$$$$$\   $$$$$$$\ 
#  $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |$$  __$$\ $$  _$$  _$$\  \____$$\ $$ |$$  __$$\ $$  _____|
#  $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |$$ |  $$ |\$$$$$$\  
#  $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |$$ |  $$ | \____$$\ 
#   $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |$$ |  $$ |$$$$$$$  |
#   \______/  \______/ \______|\__|  \__|   \__| \______/ \__| \__| \__| \_______|\__|\__|  \__|\_______/ 
"""
    print(art)

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

def sanitize_domain(domain):
    # Remove 'http://', 'https://', and 'www.' from the domain
    domain = domain.lower().replace('http://', '').replace('https://', '').replace('www.', '')
    # Extract only the main domain name
    return domain.split('/')[0]

def create_html_report(data, domain):
    sanitized_domain = sanitize_domain(domain)
    template_dir = os.path.abspath('templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('report_template.html')
    output = template.render(data=data)
    report_filename = f'{sanitized_domain}_report.html'
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(output)
    return report_filename

def main(domain):
    print_ascii_art()
    if not domain.startswith('https://'):
        domain = 'https://' + domain
    
    try:
        ip_address = resolve_domain_to_ip(domain)
        if ip_address:
            print(f"IP address: {ip_address}")

            data = {
                'domain': domain,
                'ip_address': ip_address,
                'server_location': get_server_location(ip_address),  
                'ssl_certificate': get_ssl_certificate(domain),
                'whois': get_domain_whois(domain),
                'dns_records': resolve_dns(domain),
                'headers': get_headers(domain),
                'server_info': get_server_location(domain),
                'cookies': get_cookies(domain),
                'social_tags': get_social_tags(domain),
                #'global_ranking': get_global_ranking(domain),
                'open_ports': run_nmap(ip_address), 
                'carbon_footprint': get_carbon_footprint(domain),
                'tech_stack': get_tech_stack(domain),
                'quality_metrics': get_quality_metrics(domain),
                'waf_detection': detect_waf(domain),  
                'robots_txt': fetch_robots_txt(domain),
                'sec_headers': check_security_headers(domain),
                'sitemap': fetch_sitemap(domain),
                'threat': handler(domain),
            }

            # Print data for debugging purposes
            #for key, value in data.items():
            #    print(f"{key}: {value}")

            report_filename = create_html_report(data, domain)
            print(f"Report generated: {report_filename}")

        else:
            print(f"Failed to resolve domain {domain}. No IP address found.")

    except socket.gaierror as e:
        print(f"Failed to resolve domain: {e}")

if __name__ == "__main__":
    domain = input("Enter the Domain:") 
    main(domain)
