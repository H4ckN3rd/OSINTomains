# cookies.py

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_selenium_cookies(domain):
    try:
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        driver = uc.Chrome(options=options)
        driver.get(domain)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        cookies = driver.get_cookies()
        driver.quit()
        return cookies
    except Exception as e:
        print(f"Selenium error: {e}")
        return []

def get_cookies(domain):
    try:
        client_cookies = get_selenium_cookies(domain)
        if client_cookies:
            # Format cookies data to a list of dictionaries
            formatted_cookies = []
            for cookie in client_cookies:
                formatted_cookie = {
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'domain': cookie['domain'],
                    'path': cookie['path'],
                    'expiry': cookie['expiry'],
                    'httpOnly': cookie['httpOnly'],
                    'secure': cookie['secure'],
                    'sameSite': cookie.get('sameSite', 'None')  # 'sameSite' might not always be present
                }
                formatted_cookies.append(formatted_cookie)
            return formatted_cookies
        else:
            return [{'skipped': 'No cookies'}]
    except Exception as e:
        print(f"Selenium error: {e}")
        return [{'skipped': 'Error fetching cookies'}]

if __name__ == "__main__":
    url = input("Enter the domain: ").strip()
    cookies = get_cookies(url)
    print(f"Cookies for {url}: {cookies}")
