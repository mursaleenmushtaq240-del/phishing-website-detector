# Phishing Website Detector
A simple Python tool that detects possible phishing websites.

## How it works
This script analyzes a URL for common phishing indicators (missing HTTPS, presence of '@' in URL, hyphens in domain, unusually long domains, and suspicious words like "login", "verify", "free"). It scores the URL and prints whether it looks safe, risky, or suspicious.

## Requirements
- Python 3.x
- Uses only the Python standard library (urllib.parse)

## Installation
Clone the repo:
```bash
git clone https://github.com/mursaleenmushtaq240-del/phishing-website-detector.git
cd phishing-website-detector
