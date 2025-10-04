from urllib.parse import urlparse

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
