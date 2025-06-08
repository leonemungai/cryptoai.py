import random

# Sample cryptocurrency database
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10,
        "risk_level": "medium"
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10,
        "risk_level": "medium"
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10,
        "risk_level": "low"
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10,
        "risk_level": "high"
    }
}

# Greeting messages
greetings = [
    "Hi there! Ready to explore sustainable crypto investments?",
    "Hello! Let's find you some profitable and eco-friendly crypto options.",
    "Welcome! I'm here to help you make informed crypto decisions."
]

# Response templates
responses = {
    "greeting": random.choice(greetings),
    "help": "I can help you with:\n- Trending cryptos ('What's trending?')\n- Sustainable options ('Show green coins')\n- Specific coin info ('Tell me about Bitcoin')\n- General advice ('What should I buy?')",
    "disclaimer": "⚠️ Disclaimer: Crypto investments carry risk. This is not financial advice. Always do your own research before investing.",
    "unknown": "I'm not sure I understand. Try asking about crypto trends, sustainability, or specific coins."
}

def analyze_profitability():
    """Find coins with best profitability metrics"""
    profitable_coins = []
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
            profitable_coins.append((coin, data))
    
    # Sort by market cap (high first) then sustainability
    profitable_coins.sort(key=lambda x: (x[1]["market_cap"] == "high", x[1]["sustainability_score"]), reverse=True)
    return profitable_coins

def analyze_sustainability():
    """Find coins with best sustainability metrics"""
    sustainable_coins = []
    for coin, data in crypto_db.items():
        if data["energy_use"] == "low" and data["sustainability_score"] >= 7:
            sustainable_coins.append((coin, data))
    
    # Sort by sustainability score then market cap
    sustainable_coins.sort(key=lambda x: (x[1]["sustainability_score"], x[1]["market_cap"] == "high"), reverse=True)
    return sustainable_coins

def get_coin_info(coin_name):
    """Get information about a specific coin"""
    coin_data = crypto_db.get(coin_name)
    if not coin_data:
        return None
    
    info = f"{coin_name}:\n"
    info += f"- Price trend: {coin_data['price_trend'].capitalize()}\n"
    info += f"- Market cap: {coin_data['market_cap'].capitalize()}\n"
    info += f"- Energy use: {coin_data['energy_use'].capitalize()}\n"
    info += f"- Sustainability: {coin_data['sustainability_score']}/10\n"
    info += f"- Risk level: {coin_data['risk_level'].capitalize()}"
    
    return info

def generate_advice(preference):
    """Generate investment advice based on user preference"""
    if preference == "profit":
        coins = analyze_profitability()
        if not coins:
            return "Currently no coins meet our strict profitability criteria."
        
        top_coin = coins[0]
        return (f"Based on profitability, consider {top_coin[0]} (ADA). It's currently {top_coin[1]['price_trend']} "
                f"with a {top_coin[1]['market_cap']} market cap and sustainability score of {top_coin[1]['sustainability_score']}/10.")
    
    elif preference == "sustainability":
        coins = analyze_sustainability()
        if not coins:
            return "Currently no coins meet our strict sustainability criteria."
        
        top_coin = coins[0]
        return (f"For sustainability, consider {top_coin[0]} (ADA). It has low energy use "
                f"and excellent sustainability ({top_coin[1]['sustainability_score']}/10), "
                f"with a {top_coin[1]['price_trend']} price trend.")
    
    else:  # balanced approach
        profitable = analyze_profitability()
        sustainable = analyze_sustainability()
        
        # Find coins that appear in both lists
        best_options = []
        for p_coin in profitable[:3]:
            for s_coin in sustainable[:3]:
                if p_coin[0] == s_coin[0]:
                    best_options.append(p_coin)
        
        if not best_options:
            return "It's challenging to find coins excelling in both areas right now. You might need to prioritize either profit or sustainability."
        
        top_coin = best_options[0]
        return (f"For balanced growth, {top_coin[0]} (ADA) stands out. It's {top_coin[1]['price_trend']}, "
                f"has a {top_coin[1]['market_cap']} market cap, and scores {top_coin[1]['sustainability_score']}/10 "
                "for sustainability.")

def chatbot_response(user_input):
    """Process user input and generate appropriate response"""
    user_input = user_input.lower()
    
    # Greeting
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return responses["greeting"] + "\n" + responses["help"]
    
    # Help
    if "help" in user_input:
        return responses["help"]
    
    # Trending coins
    if any(word in user_input for word in ["trend", "rising", "upward", "profit"]):
        coins = analyze_profitability()
        if not coins:
            return "No coins are currently showing strong upward trends."
        
        response = "Currently trending (rising price with solid market cap):\n"
        for coin, data in coins[:3]:  # Show top 3
            response += f"- {coin}: {data['price_trend']} price, {data['market_cap']} market cap, sustainability {data['sustainability_score']}/10\n"
        return response + responses["disclaimer"]
    
    # Sustainable coins
    if any(word in user_input for word in ["sustain", "green", "eco", "environment"]):
        coins = analyze_sustainability()
        if not coins:
            return "No coins currently meet our high sustainability standards."
        
        response = "Top sustainable options (low energy use, high sustainability score):\n"
        for coin, data in coins[:3]:  # Show top 3
            response += f"- {coin}: sustainability {data['sustainability_score']}/10, {data['price_trend']} price, {data['market_cap']} market cap\n"
        return response + responses["disclaimer"]
    
    # Specific coin info
    for coin in crypto_db.keys():
        if coin.lower() in user_input:
            info = get_coin_info(coin)
            if info:
                return info + "\n" + responses["disclaimer"]
            break
    
    # General advice
    if any(word in user_input for word in ["advice", "recommend", "suggest", "buy", "invest"]):
        if "profit" in user_input:
            return generate_advice("profit") + "\n" + responses["disclaimer"]
        elif "sustain" in user_input or "green" in user_input:
            return generate_advice("sustainability") + "\n" + responses["disclaimer"]
        else:
            return generate_advice("balanced") + "\n" + responses["disclaimer"]
    
    # Fallback
    return responses["unknown"] + "\n" + responses["help"]

# Main chat loop
print("CryptoAdvisor: " + responses["greeting"])
print("Type 'help' for options or ask me anything about cryptocurrencies!")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("CryptoAdvisor: Happy investing! Remember to diversify and do your own research. Goodbye!")
        break
    
    response = chatbot_response(user_input)
    print("CryptoAdvisor:", response)