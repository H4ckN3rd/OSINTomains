```
   $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\                                $$\                     
  $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|                               \__|                    
  $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\ $$$$$$$\   $$$$$$$\ 
  $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |$$  __$$\ $$  _$$  _$$\  \____$$\ $$ |$$  __$$\ $$  _____|
  $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |$$ |  $$ |\$$$$$$\  
  $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |$$ |  $$ | \____$$\ 
   $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |$$ |  $$ |$$$$$$$  |
   \______/  \______/ \______|\__|  \__|   \__| \______/ \__| \__| \__| \_______|\__|\__|  \__|\_______/ 

```
**Developers:** Jatin, Joy, Arpit

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Output](#output)

## Project Overview

OSINTomains is an Open Source Intelligence (OSINT) tool designed to gather a variety of information about a given domain. This tool performs comprehensive checks and generates an HTML report containing detailed insights about the domain.

## Features

- SSL Certificate Information
- Carbon Footprint Analysis
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

## Screenshots

![image](https://github.com/jatink2004/OSINTomains/blob/master/Screenshots/SS1.png?raw=true)
![image](https://github.com/jatink2004/OSINTomains/blob/master/Screenshots/SS2.png?raw=true)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jatink2004/OSINTomains.git
    cd OSINTomains
    ```

2. **API Keys Setup**

   Get API Keys

   - Obtain your Google API key [Here](https://developers.google.com/speed/docs/insights/v5/get-started).
   - Get your Cloudmersive API key [Here](https://portal.cloudmersive.com/keys).

   Configure Environment Variables

   To set up your API keys:

   1. In the root directory of your project, create a `.env` file if it doesn't exist.

   2. Add the following content to the `.env` file:

      ```sh
      CLOUDMERSIVE_API_KEY="YOUR_CLOUDMERSIVE_API_KEY"
      GOOGLE_CLOUD_API_KEY="YOUR_GOOGLE_CLOUD_API_KEY"
      ```

      Replace `"YOUR_CLOUDMERSIVE_API_KEY"` and `"YOUR_GOOGLE_CLOUD_API_KEY"` with the API keys you obtained in the previous step.

3. Install the required dependencies:
    ```sh
    pip3 install -r requirements.txt
    ```

4. Ensure the `templates` directory contains `report_template.html'


## Usage

1. Before running the script, ensure that `nmap` is installed. If not, you can download and install it from [nmap.org](https://nmap.org/download).

2. Run the main script:
    ```sh
    python .\main.py
    ```

3. Enter the domain when prompted:
    ```sh
    Enter the Domain: https://example.com
    ```
    
4. Upon completion, an HTML report will be generated in the root directory of the project. The report filename will be based on the domain (e.g., `example_report.html`).

## Output

The output of the tool is an HTML report (`domain_report.html`), which includes:

- **Domain Information**: Basic details about the domain.
- **IP Address**: The resolved IP address of the domain.
- **Server Location**: Geographical location of the server.
- **SSL Certificate Details**: Information about the domain's SSL certificate.
- **WHOIS Information**: Ownership and registration details.
- **DNS Records**: Details of DNS records associated with the domain.
- **HTTP Headers**: HTTP headers returned by the domain's server.
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
