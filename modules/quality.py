import requests

def get_quality_metrics(domain):
    api_key = "AIzaSyDV7vy409kfDJjBoqSK_UAu8aLLt4GxryU"
    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://{domain}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        metrics = {
            "performance_score": data["lighthouseResult"]["categories"]["performance"]["score"],
            "accessibility_score": data["lighthouseResult"]["categories"]["accessibility"]["score"],
            "best_practices_score": data["lighthouseResult"]["categories"]["best-practices"]["score"],
            "seo_score": data["lighthouseResult"]["categories"]["seo"]["score"],
            "pwa_score": data["lighthouseResult"]["categories"]["pwa"]["score"]
        }
        return metrics
    else:
        return "Could not retrieve quality metrics"

