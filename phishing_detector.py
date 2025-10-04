#!/usr/bin/env python3
"""
phishing_detector.py
Simple heuristic-based phishing URL checker (no external libraries).
Usage:
    python phishing_detector.py https://example.com
Or run without args to enter URLs interactively.
"""

from urllib.parse import urlparse
import argparse
import sys

SUSPICIOUS_WORDS = [
    "login", "verify", "update", "secure", "account", "bank",
    "confirm", "password", "signin", "reset", "activate", "free",
    "bonus", "win"
]

def score_url(url: str) -> int:
    """Return a heuristic score. Higher = more suspicious."""
    url_lower = url.lower()
    parsed = urlparse(url_lower)
    domain = parsed.netloc or parsed.path  # fallback if schema missing

    score = 0

    # 1. Missing HTTPS
    if not url_lower.startswith("https://"):
        score += 1

    # 2. Contains '@' (often used in phishing traps)
    if "@" in url_lower:
        score += 1

    # 3. Dash in domain (hyphenated domains sometimes suspicious)
    if "-" in domain:
        score += 1

    # 4. Long domain (very long domains are suspicious)
    if len(domain) > 25:
        score += 1

    # 5. IP address used instead of domain
    parts = domain.split('.')
    if all(p.isdigit() for p in parts if p):
        score += 1

    # 6. Suspicious keywords in URL path or query
    if any(word in url_lower for word in SUSPICIOUS_WORDS):
        score += 1

    # 7. Many subdomains (like random-sub.example.co.uk)
    if domain.count('.') >= 4:
        score += 1

    return score

def verdict_from_score(score: int) -> str:
    if score >= 4:
        return "Suspicious (possible phishing)"
    if score == 3:
        return "Risky — check carefully"
    return "Likely safe"

def analyze(url: str) -> None:
    sc = score_url(url)
    v = verdict_from_score(sc)
    print(f"\nURL: {url}")
    print(f"Score: {sc}")
    print(f"Verdict: {v}")

def interactive_loop():
    print("Enter URL to analyze (empty line to quit):")
    try:
        while True:
            url = input("> ").strip()
            if not url:
                break
            # add scheme if omitted
            if "://" not in url:
                url = "http://" + url
            analyze(url)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")

def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple phishing URL heuristic checker")
    parser.add_argument("url", nargs="?", help="URL to check (optional). If omitted, runs interactive mode.")
    args = parser.parse_args(argv)

    if args.url:
        url = args.url
        if "://" not in url:
            url = "http://" + url
        analyze(url)
    else:
        interactive_loop()

if _name_ == "_main_":
    main()
