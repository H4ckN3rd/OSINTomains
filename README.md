# OSINTomains

**Developers:** Jatin, Joy, Arpit

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modules](#modules)
6. [Output](#output)
7. [Dependencies](#dependencies)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)

## Project Overview

OSINTomains is an Open Source Intelligence (OSINT) tool designed to gather a variety of information about a given domain. This tool performs comprehensive checks and generates an HTML report containing detailed insights about the domain.

## Features

- SSL Certificate Information
- Carbon Footprint Analysis
- Cookie Details
- DNS Records
- WHOIS Information
- Web Application Firewall Detection
- HTTP Headers
- Nmap Port Scanning
- Quality Metrics
- Robots.txt Analysis
- Security Headers Check
- Server Location Information
- Sitemap Retrieval
- Social Media Tags
- Threat Analysis
- Technology Stack Detection

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/OSINTomains.git
    cd OSINTomains
    ```

2. In the root directory, create a .env file and add the following content:
   ```sh 
    CLOUDMERSIVE_API_KEY="YOUR_CLOUDMERSIVE_API_KEY"
    GOOGLE_CLOUD_API_KEY="YOUR_GOOGLE_CLOUD_API_KEY"
   ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure the `templates` directory contains `report_template.html` and the `static` directory contains `styles.css`.

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Enter the domain when prompted:
    ```sh
    Enter the Domain: https://example.com
    ```
    
3. Upon completion, an HTML report will be generated in the root directory of the project. The report filename will be based on the domain (e.g., `example_report.html`).

## Modules

### SSL Certificate Information

- **File:** `modules/certificate.py`
- **Function:** `get_ssl_certificate(domain)`

### Carbon Footprint Analysis

- **File:** `modules/carbon_footprint.py`
- **Function:** `get_carbon_footprint(domain)`

### Cookie Details

- **File:** `modules/cookies.py`
- **Function:** `get_cookies(domain)`

### DNS Records

- **File:** `modules/dns_info.py`
- **Function:** `resolve_dns(domain)`

### WHOIS Information

- **File:** `modules/domain_info.py`
- **Function:** `get_domain_whois(domain)`

### Web Application Firewall Detection

- **File:** `modules/firewall.py`
- **Function:** `detect_waf(domain)`

### HTTP Headers

- **File:** `modules/headers.py`
- **Function:** `get_headers(domain)`

### Nmap Port Scanning

- **File:** `modules/nmap.py`
- **Function:** `run_nmap(ip_address)`

### Quality Metrics

- **File:** `modules/quality.py`
- **Function:** `get_quality_metrics(domain)`

### Robots.txt Analysis

- **File:** `modules/robots.py`
- **Function:** `fetch_robots_txt(domain)`

### Security Headers Check

- **File:** `modules/sec_headers.py`
- **Function:** `check_security_headers(domain)`

### Server Location Information

- **File:** `modules/server_info.py`
- **Function:** `get_server_location(ip_address)`

### Sitemap Retrieval

- **File:** `modules/sitemap.py`
- **Function:** `fetch_sitemap(domain)`

### Social Media Tags

- **File:** `modules/social_tags.py`
- **Function:** `get_social_tags(domain)`

### Threat Analysis

- **File:** `modules/threats.py`
- **Function:** `handler(domain)`

### Technology Stack Detection

- **File:** `modules/tech_stack.py`
- **Function:** `get_tech_stack(domain)`

## Output

The output of the tool is an HTML report (`domain_report.html`), which includes:

- **Domain Information**: Basic details about the domain.
- **IP Address**: The resolved IP address of the domain.
- **Server Location**: Geographical location of the server.
- **SSL Certificate Details**: Information about the domain's SSL certificate.
- **WHOIS Information**: Ownership and registration details.
- **DNS Records**: Details of DNS records associated with the domain.
- **HTTP Headers**: HTTP headers returned by the domain's server.
- **Cookies**: Information about cookies set by the domain.
- **Social Media Tags**: Open Graph and Twitter Card tags.
- **Open Ports**: Results from an Nmap scan of the domain's IP address.
- **Carbon Footprint**: Estimate of the domain's carbon footprint.
- **Technology Stack**: Technologies used by the domain.
- **Quality Metrics**: Various quality metrics of the domain.
- **WAF Detection**: Detection of any web application firewalls.
- **Robots.txt Content**: Content of the domain's robots.txt file.
- **Security Headers**: Security-related HTTP headers.
- **Sitemap URLs**: URLs listed in the domain's sitemap.
- **Threat Analysis**: Analysis of potential threats associated with the domain.

## Dependencies

- Python 3.x
- `requests`
- `jinja2`
- `xml.etree.ElementTree`
- `socket`
- `time`
- `urllib.parse`
- Other dependencies specified in `requirements.txt`
