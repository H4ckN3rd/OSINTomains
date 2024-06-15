import subprocess

def run_nmap(domain):
    try:
        result = subprocess.run(['nmap', '-A', domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running Nmap scan for {domain}: {e}")
        return None
