import subprocess

def run_traceroute(ip_address):
    try:
        # Use shell=True to execute traceroute command via shell (for Windows compatibility)
        result = subprocess.run(['traceroute', '-p', '8080', ip_address], capture_output=True, text=True, shell=True)
        return result.stdout
    except Exception as e:
        return str(e)


