import asyncio
from pyppeteer import launch
import requests
from urllib.parse import urlparse

async def get_puppeteer_cookies(url):
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    try:
        navigation_promise = page.goto(url, {'waitUntil': 'networkidle2'})
        timeout_promise = asyncio.sleep(3)
        await asyncio.wait([navigation_promise, timeout_promise], return_when=asyncio.FIRST_COMPLETED)
        cookies = await page.cookies()
    finally:
        await browser.close()
    return cookies

def get_cookies(domain):
    parsed_url = urlparse(domain)
    if not parsed_url.scheme:
        url = f'http://{domain}'
    else:
        url = domain

    header_cookies = None
    client_cookies = None

    try:
        response = requests.get(url, allow_redirects=True)
        header_cookies = response.headers.get('set-cookie')
    except requests.RequestException as e:
        print(f"Request error: {e}")

    try:
        client_cookies = asyncio.get_event_loop().run_until_complete(get_puppeteer_cookies(url))
    except Exception as e:
        print(f"Puppeteer error: {e}")

    if not header_cookies and not client_cookies:
        return {'skipped': 'No cookies'}

    return {'headerCookies': header_cookies, 'clientCookies': client_cookies}

if __name__ == "__main__":
    domain = input("Enter the Domain: ")
    cookies = get_cookies(domain)
    if cookies:
        print(f"Cookies for {domain}: {cookies}")
    else:
        print("Failed to retrieve cookies information.")
