# 🎯 Phishing Website Detector

Developed by *Mursaleen Mushtaq*

---

## 📘 Project Overview
The *Phishing Website Detector* is a machine learning-based project designed to detect and classify phishing websites.  
It analyzes various features of a website (like URL length, HTTPS status, domain age, and more) to predict whether the site is *legitimate or phishing*.

This project demonstrates how machine learning can be used to improve *cybersecurity awareness* and help protect users from online scams.

---

## 🚀 Features
- Detects phishing websites using trained ML models  
- Extracts and analyzes key website attributes  
- Simple and user-friendly interface  
- Demonstrates practical application of cybersecurity concepts  

---

## 🧠 Technologies Used
- *Python*
- *Scikit-learn*
- *Pandas*
- *NumPy*
- *Flask*
- *HTML, CSS*

---

## ⚙️ How It Works
1. The user enters a website URL.  
2. The system extracts several features (like presence of HTTPS, URL length, etc.).  
3. The trained ML model analyzes the data.  
4. The result is displayed as *“Phishing”* or *“Legitimate.”*

---

## 📂 Project Structure
The program checks the following:
- Missing HTTPS  
- Use of special symbols like @  
- Suspicious words (like login, verify, secure, etc.)  
- Very long or strange domain names  
- Use of hyphens or numbers in the domain  

Each point adds to a “risk score,” and finally, the program decides if the link is Safe, Suspicious, or Risky.

*Example Output:*
