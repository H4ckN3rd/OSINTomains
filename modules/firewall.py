import requests

def has_waf(waf):
    return {
        'hasWaf': True,
        'waf': waf
    }

def detect_waf(url):
    full_url = url if url.startswith('http') else f'http://{url}'
    
    try:
        response = requests.get(full_url)
        headers = response.headers

        if 'server' in headers:
            if 'cloudflare' in headers['server']:
                return has_waf('Cloudflare')
            if 'AkamaiGHost' in headers['server']:
                return has_waf('Akamai')
            if 'Sucuri' in headers['server']:
                return has_waf('Sucuri')
            if 'BarracudaWAF' in headers['server']:
                return has_waf('Barracuda WAF')
            if 'F5 BIG-IP' in headers['server'] or 'BIG-IP' in headers['server']:
                return has_waf('F5 BIG-IP')
            if 'FortiWeb' in headers['server']:
                return has_waf('Fortinet FortiWeb WAF')
            if 'Imperva' in headers['server']:
                return has_waf('Imperva SecureSphere WAF')
            if 'Safe3WAF' in headers['server']:
                return has_waf('Safe3 Web Application Firewall')
            if 'NAXSI' in headers['server']:
                return has_waf('NAXSI WAF')
            if 'QRATOR' in headers['server']:
                return has_waf('QRATOR WAF')
            if 'ddos-guard' in headers['server']:
                return has_waf('DDoS-Guard WAF')
            if 'Yundun' in headers['server']:
                return has_waf('Yundun WAF')

        if 'x-powered-by' in headers and 'AWS Lambda' in headers['x-powered-by']:
            return has_waf('AWS WAF')

        if 'x-sucuri-id' in headers or 'x-sucuri-cache' in headers:
            return has_waf('Sucuri CloudProxy WAF')

        if 'x-protected-by' in headers and 'Sqreen' in headers['x-protected-by']:
            return has_waf('Sqreen')

        if 'x-waf-event-info' in headers:
            return has_waf('Reblaze WAF')

        if 'set-cookie' in headers and '_citrix_ns_id' in headers['set-cookie']:
            return has_waf('Citrix NetScaler')

        if 'x-denied-reason' in headers or 'x-wzws-requested-method' in headers:
            return has_waf('WangZhanBao WAF')

        if 'x-webcoment' in headers:
            return has_waf('Webcoment Firewall')

        if 'x-yd-waf-info' in headers or 'x-yd-info' in headers:
            return has_waf('Yundun WAF')

        if 'x-datapower-transactionid' in headers:
            return has_waf('IBM WebSphere DataPower')

        return {'hasWaf': False}

    except requests.RequestException as error:
        return {
            'error': f"An error occurred while detecting WAF: {error}"
        }

if __name__ == "__main__":
    domain = input("Enter the Domain: ")
    waf_info = detect_waf(domain)
    if waf_info['hasWaf']:
        print(f"WAF detected for {domain}: {waf_info['waf']}")
    else:
        print(f"No WAF detected for {domain}.")
