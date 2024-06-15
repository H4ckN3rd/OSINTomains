from similarweb import Similarweb

def get_global_ranking(domain):
    try:
        api_key = 'your_similarweb_api_key_here'  # Replace with your Similarweb API key
        similarweb = Similarweb(api_key)
        response = similarweb.global_rank(domain)
        
        if response.get('meta', {}).get('status') == 200:
            ranking = response.get('global_rank')
            return ranking
        else:
            return "Could not retrieve global ranking"

    except Exception as e:
        print(f"Error retrieving global ranking for {domain}: {e}")
        return "Could not retrieve global ranking"
