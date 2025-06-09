# cryptoai.py

📌 Overview
CryptoAdvisor is a rule-based chatbot that analyzes cryptocurrency data to provide investment advice based on profitability (price trends, market cap) and sustainability (energy efficiency, project viability). This Python-based tool helps users make more informed crypto investment decisions by evaluating both financial and environmental factors.

✨ Features
Dual-Factor Analysis: Evaluates coins based on both profitability and sustainability metrics

Predefined Dataset: Comes with sample data for Bitcoin, Ethereum, and Cardano

Customizable Rules: Easy-to-modify recommendation logic

User-Friendly Interface: Simple text-based interaction

Educational Value: Helps users understand sustainable crypto investing

🛠️ Installation
Ensure you have Python 3.6+ installed

Clone this repository or copy the chatbot code

No additional dependencies required for basic version

🚀 Quick Start
Run the Python script containing the chatbot code

Interact with the bot by typing questions like:

"Which crypto is trending up?"

"What's the most sustainable coin?"

"What should I buy for long-term growth?"

💡 How It Works
Core Components:
Cryptocurrency Database:

python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    # ... other coins
}
Analysis Logic:

Profitability: price_trend = "rising" and market_cap = "high"

Sustainability: energy_use = "low" and sustainability_score > 7/10

Response System:

python
if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"Invest in {recommend}! 🌱")
📋 Sample Conversation
text
You: Which crypto should I buy for long-term growth?
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀
🎯 Stretch Goals (Optional Enhancements)
API Integration: Connect to CoinGecko's API for real-time data

NLP Enhancement: Implement NLTK for more natural language understanding

Risk Disclaimers: Add automated investment warnings

Portfolio Suggestions: Generate diversified portfolio recommendations

⚠️ Disclaimer
This chatbot provides educational information only, not financial advice. Cryptocurrency investments carry substantial risk. Always conduct your own research before making investment decisions.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit pull requests for:

Additional cryptocurrency data

Improved analysis algorithms

Enhanced user interaction features

