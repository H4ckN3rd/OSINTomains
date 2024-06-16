from Wappalyzer import Wappalyzer, WebPage

def get_tech_stack(domain):
    try:
        wappalyzer = Wappalyzer.latest()
        url = f"{domain}"
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze(webpage)
        if not technologies:
            raise Exception('Unable to find any technologies for site')
        return technologies
    except Exception as e:
        print(f"Error retrieving tech stack for {domain}: {e}")
        return None
    
if __name__ == "__main__":
    test_url = input("Enter the URL: ")  # Replace with the URL you want to analyze
    try:
        metrics = get_tech_stack(test_url)
        print(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")
