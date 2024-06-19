import os
import requests

def get_quality_metrics(url):
    api_key = os.getenv('GOOGLE_CLOUD_API_KEY')

    if not api_key:
        raise ValueError('Missing Google API. You need to set the `GOOGLE_CLOUD_API_KEY` environment variable')

    endpoint = (
        f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?"
        f"url={url}&category=PERFORMANCE&category=ACCESSIBILITY"
        f"&category=BEST_PRACTICES&category=SEO&category=PWA&strategy=mobile"
        f"&key={api_key}"
    )

    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def parse_metrics(data):
    # Extract key metrics
    metrics = {}
    lighthouse = data.get('lighthouseResult', {})
    
    # Example metrics to extract (add more as needed)
    audits = lighthouse.get('audits', {})
    metrics['First Contentful Paint'] = audits.get('first-contentful-paint', {}).get('displayValue', 'N/A')
    metrics['Speed Index'] = audits.get('speed-index', {}).get('displayValue', 'N/A')
    metrics['Largest Contentful Paint'] = audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A')
    metrics['Interactive'] = audits.get('interactive', {}).get('displayValue', 'N/A')
    metrics['Total Blocking Time'] = audits.get('total-blocking-time', {}).get('displayValue', 'N/A')
    metrics['Cumulative Layout Shift'] = audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A')

    return metrics

def create_html_report(metrics, filename='report.html'):
    html_content = "<html><body><h1>Page Quality Metrics</h1><table border='1'>"
    for metric, value in metrics.items():
        html_content += f"<tr><td>{metric}</td><td>{value}</td></tr>"
    html_content += "</table></body></html>"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_report(url, filename='report.html'):
    try:
        data = get_quality_metrics(url)
        metrics = parse_metrics(data)
        create_html_report(metrics, filename)
        print(f"Report generated successfully: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the domain: ").strip()
    qualtity = get_quality_metrics(url)
    print(f"Cookies for {url}: {qualtity}")
