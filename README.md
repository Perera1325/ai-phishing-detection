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


## Project Overview

This project is an AI-powered phishing detection system capable of identifying
both phishing emails and malicious URLs. It uses Machine Learning and Natural
Language Processing techniques to analyze user inputs and classify them as
SAFE or PHISHING.

The system is designed as a command-line automation tool and demonstrates
real-world cybersecurity use cases.



## System Architecture

1. Dataset Collection
   - Real-world phishing datasets collected from Kaggle
   - Manual labeling and preprocessing

2. Email Phishing Detection
   - Text cleaning and normalization
   - TF-IDF feature extraction
   - Machine Learning classification

3. URL Phishing Detection
   - URL lexical feature extraction
   - Random Forest classifier

4. Automation Layer
   - Command-line interface
   - Real-time phishing prediction




## How to Run

1. Clone the repository
```bash
git clone https://github.com/perera1325/ai-phishing-detection.git
cd ai-phishing-detection



---

### 🛠 Technologies Used
```markdown
## Technologies Used

- Python
- Scikit-learn
- NLP (TF-IDF)
- Pandas, NumPy
- Random Forest, Logistic Regression
- Kali Linux
- Git & GitHub



## Key Learning Outcomes

- Built an end-to-end cybersecurity ML project
- Applied NLP techniques for text classification
- Designed ML pipelines for phishing detection
- Integrated multiple ML models into one system
- Gained hands-on experience with GitHub and Linux




## Future Improvements

- Web-based interface using Flask or FastAPI
- Deep Learning models (LSTM / BERT)
- Real-time email inbox integration
- Browser extension for URL detection
- Model performance optimization
