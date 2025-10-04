[8:09 pm, 04/10/2025] Mursaleen mushtaq: from urllib.parse import urlparse

def phishing_detector(url):
    suspicious_words = ['login', 'verify', 'update', 'free', 'bonus', 'win', 'secure', 'bank', 'account']
    parsed = urlparse(url)
    domain = parsed.netloc

    # Checks
    has_https = url.startswith("https")
    contains_at = '@' in url
    contains_dash = '-' in domain
    long_domain = len(domain) > 25
    suspicious_word = any(word in url.lower() for word in suspicious_words)

    # Score system
    score = 0
    if not has_https: score += 1
    if contains_at: score += 1
    if contains_dash: score += 1
    if long_domain: score += 1
    if suspicious_word: score += 1

    print("\nAnalyzing:", url)
    if score >= 3:
        print("⚠️ This website looks Suspicious (Possible Phishing).")
    elif score == 2:
        print("⚠️ This website might be risky, check carefully.")
    else:
        print("✅ This website looks Safe.")

# Example run
url_input = input("Enter a website URL: ")
phishing_detector(url_input)
[9:13 pm, 04/10/2025] Mursaleen mushtaq: # Phishing Website Detector

Ye ek simple Python project hai jo phishing websites detect karta hai.

## Kaise kaam karta hai
- User ek website URL enter karta hai.
- Program kuch suspicious patterns check karta hai (https, @, dash, long domain, suspicious words).
- Score ke hisaab se result dikhaya jata hai: Safe / Might be risky / Suspicious.

## Example
Enter a website URL: https://facebook.com  
→ Safe website detected

Enter a website URL: http://free-bonus-login-secure.win  
→ Possible phishing website detected

## Tools
- Python 3
- urllib library

## Author
Mursaleen Mushtaq
