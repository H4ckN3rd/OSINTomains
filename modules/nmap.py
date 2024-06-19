import subprocess
import nmap


def run_nmap(domain):
    try:
        result = subprocess.run(['nmap', '--traceroute', domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running Nmap scan for {domain}: {e}")
        return None
    
if __name__ == "__main__":
    domain = input("Enter the domain: ")
    nmap = run_nmap(domain)
    print(nmap)