from urllib.parse import urlparse
import dns.resolver

def fetch_mail_config(domain):
    try:
        domain = urlparse(domain).hostname or urlparse(domain).path

        # Get MX records
        mx_records = dns.resolver.resolve(domain, 'MX')

        # Get TXT records
        txt_records = dns.resolver.resolve(domain, 'TXT')

        # Filter for only email related TXT records
        email_txt_records = [
            str(record) for record in txt_records 
            if any(record.to_text().startswith(prefix) for prefix in ['v=spf1', 'v=DKIM1', 'v=DMARC1',
                                                                      'protonmail-verification=', 
                                                                      'google-site-verification=',
                                                                      'MS=', 'zoho-verification=',
                                                                      'titan-verification=', 'bluehost.com'])
        ]

        # Identify specific mail services
        mail_services = []
        for record in email_txt_records:
            if record.startswith('protonmail-verification='):
                mail_services.append({'provider': 'ProtonMail', 'value': record.split('=')[1]})
            elif record.startswith('google-site-verification='):
                mail_services.append({'provider': 'Google Workspace', 'value': record.split('=')[1]})
            elif record.startswith('MS='):
                mail_services.append({'provider': 'Microsoft 365', 'value': record.split('=')[1]})
            elif record.startswith('zoho-verification='):
                mail_services.append({'provider': 'Zoho', 'value': record.split('=')[1]})
            elif record.startswith('titan-verification='):
                mail_services.append({'provider': 'Titan', 'value': record.split('=')[1]})
            elif 'bluehost.com' in record:
                mail_services.append({'provider': 'BlueHost', 'value': record})

        # Check MX records for Yahoo
        yahoo_mx = [record.exchange.to_text() for record in mx_records if 'yahoodns.net' in record.exchange.to_text()]
        if yahoo_mx:
            mail_services.append({'provider': 'Yahoo', 'value': yahoo_mx[0]})

        # Check MX records for Mimecast
        mimecast_mx = [record.exchange.to_text() for record in mx_records if 'mimecast.com' in record.exchange.to_text()]
        if mimecast_mx:
            mail_services.append({'provider': 'Mimecast', 'value': mimecast_mx[0]})

        return {
            'mx_records': [str(record.exchange) for record in mx_records],
            'txt_records': email_txt_records,
            'mail_services': mail_services
        }

    except dns.resolver.NoAnswer:
        return {'skipped': 'No mail server in use on this domain'}

    except dns.resolver.NXDOMAIN:
        return {'skipped': 'Domain not found'}

    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    test_domain = input("Enter the domain: ")  
    try:
        metrics = fetch_mail_config(test_domain)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")