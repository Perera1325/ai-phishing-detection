## Day 02 – Dataset Collection

- Collected multiple real-world phishing email datasets from Kaggle
- Sources include Enron, SpamAssassin, Nazario, Nigerian Fraud
- Raw datasets are excluded from GitHub via .gitignore
- Data is loaded and processed locally for ML training


## Day 04 – Model Training
- Trained Logistic Regression and Naive Bayes models
- Evaluated using accuracy, precision, recall, and F1-score
- Selected and saved best performing model

## Day 05 – Email Phishing Detection Automation

- Implemented a command-line phishing email detection tool
- Loaded trained Machine Learning model and TF-IDF vectorizer
- Performed real-time phishing prediction on user-provided email text
- Applied the same preprocessing pipeline used during training
- Displayed clear SAFE / PHISHING results to the user

### Features
- Real-time email phishing detection
- NLP-based text preprocessing
- Machine Learning model inference
- User-friendly CLI interface

###  Example
Input:


## Day 06 – URL Phishing Detection & System Integration

- Designed and implemented URL feature extraction module
- Extracted lexical URL features such as length, dots, hyphens, HTTPS usage, and IP presence
- Trained a Random Forest classifier for URL phishing detection
- Integrated URL phishing detection with existing email phishing system
- Extended CLI tool to support both Email and URL phishing analysis

### URL Features Used
- URL length
- Number of dots and hyphens
- Presence of HTTPS
- Presence of IP address
- Path and query length

### Example
Input: https://secure-login-paypal.com/verify

OUtput : 

  
### System Capability
- Unified phishing detection system for both Emails and URLs
- Modular design for easy future extensions


