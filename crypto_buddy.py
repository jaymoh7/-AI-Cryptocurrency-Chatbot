import random
import time
from datetime import datetime

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "current_price": 67500,
                "description": "The original cryptocurrency and digital gold"
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "current_price": 3200,
                "description": "Smart contract platform powering DeFi"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "current_price": 0.45,
                "description": "Research-driven blockchain with proof-of-stake"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "current_price": 145,
                "description": "High-speed blockchain for DeFi and NFTs"
            },
            "Polygon": {
                "symbol": "MATIC",
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "current_price": 0.75,
                "description": "Ethereum scaling solution"
            },
            "Chainlink": {
                "symbol": "LINK",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7,
                "current_price": 15.50,
                "description": "Decentralized oracle network"
            }
        }
        
        self.greetings = [
            "🚀 Hey there, crypto explorer! I'm CryptoBuddy, your AI-powered financial sidekick!",
            "👋 Welcome to the crypto universe! I'm here to help you navigate the digital gold rush!",
            "💎 Hello, future crypto millionaire! Ready to find your next gem?"
        ]
        
        self.farewells = [
            "🌟 Happy investing! Remember: DYOR (Do Your Own Research)!",
            "💰 May your portfolio be green and your gains be massive!",
            "🚀 Catch you on the moon! Stay safe out there!"
        ]

    def greet(self):
        """Welcome message for the chatbot"""
        greeting = random.choice(self.greetings)
        print(f"\n{greeting}")
        print("\n" + "="*60)
        print("🔍 I can help you with:")
        print("• Finding profitable cryptocurrencies")
        print("• Sustainable/eco-friendly crypto recommendations")
        print("• Market trend analysis")
        print("• Comparing different cryptocurrencies")
        print("• General crypto advice and info")
        print("="*60)
        print("\n💡 Try asking: 'What's the most sustainable crypto?' or 'Which coins are trending up?'")
        print("📝 Type 'help' for more options or 'quit' to exit\n")

    def get_sustainable_cryptos(self):
        """Find the most sustainable cryptocurrencies"""
        sustainable_coins = []
        for coin, data in self.crypto_db.items():
            if data["sustainability_score"] >= 7:
                sustainable_coins.append((coin, data["sustainability_score"]))
        
        sustainable_coins.sort(key=lambda x: x[1], reverse=True)
        return sustainable_coins

    def get_trending_cryptos(self):
        """Find cryptocurrencies with rising price trends"""
        trending_coins = []
        for coin, data in self.crypto_db.items():
            if data["price_trend"] == "rising":
                trending_coins.append(coin)
        return trending_coins

    def get_low_energy_cryptos(self):
        """Find cryptocurrencies with low energy consumption"""
        low_energy_coins = []
        for coin, data in self.crypto_db.items():
            if data["energy_use"] == "low":
                low_energy_coins.append(coin)
        return low_energy_coins

    def compare_cryptos(self, coin1, coin2):
        """Compare two cryptocurrencies"""
        if coin1 not in self.crypto_db or coin2 not in self.crypto_db:
            return "❌ Sorry, I don't have data for one or both of those cryptocurrencies."
        
        data1 = self.crypto_db[coin1]
        data2 = self.crypto_db[coin2]
        
        comparison = f"\n📊 Comparison: {coin1} ({data1['symbol']}) vs {coin2} ({data2['symbol']})\n"
        comparison += "="*60 + "\n"
        comparison += f"💰 Current Price:     ${data1['current_price']:,} vs ${data2['current_price']:,}\n"
        comparison += f"📈 Price Trend:       {data1['price_trend'].title()} vs {data2['price_trend'].title()}\n"
        comparison += f"🏦 Market Cap:        {data1['market_cap'].title()} vs {data2['market_cap'].title()}\n"
        comparison += f"⚡ Energy Usage:      {data1['energy_use'].title()} vs {data2['energy_use'].title()}\n"
        comparison += f"🌱 Sustainability:    {data1['sustainability_score']}/10 vs {data2['sustainability_score']}/10\n"
        comparison += "="*60 + "\n"
        
        # Add recommendation based on comparison
        if data1['sustainability_score'] > data2['sustainability_score'] and data1['price_trend'] == 'rising':
            comparison += f"🌟 WINNER: {coin1} - Better sustainability and rising trend!\n"
        elif data2['sustainability_score'] > data1['sustainability_score'] and data2['price_trend'] == 'rising':
            comparison += f"🌟 WINNER: {coin2} - Better sustainability and rising trend!\n"
        elif data1['price_trend'] == 'rising' and data2['price_trend'] != 'rising':
            comparison += f"📈 EDGE: {coin1} - Currently trending upward\n"
        elif data2['price_trend'] == 'rising' and data1['price_trend'] != 'rising':
            comparison += f"📈 EDGE: {coin2} - Currently trending upward\n"
        elif data1['sustainability_score'] > data2['sustainability_score']:
            comparison += f"🌱 EDGE: {coin1} - More environmentally friendly\n"
        elif data2['sustainability_score'] > data1['sustainability_score']:
            comparison += f"🌱 EDGE: {coin2} - More environmentally friendly\n"
        else:
            comparison += "⚖️ Both cryptocurrencies have similar profiles\n"
            
        comparison += "\n💡 Consider your investment goals: short-term gains vs long-term sustainability!"
        
        return comparison

    def get_crypto_info(self, crypto_name):
        """Get detailed information about a specific cryptocurrency"""
        # Check if the crypto exists (case-insensitive)
        crypto_found = None
        for coin in self.crypto_db:
            if coin.lower() == crypto_name.lower():
                crypto_found = coin
                break
        
        if not crypto_found:
            return f"❌ Sorry, I don't have information about {crypto_name} in my database."
        
        data = self.crypto_db[crypto_found]
        info = f"\n💎 {crypto_found} ({data['symbol']}) Analysis\n"
        info += "="*40 + "\n"
        info += f"💰 Current Price: ${data['current_price']}\n"
        info += f"📈 Price Trend: {data['price_trend']}\n"
        info += f"🏦 Market Cap: {data['market_cap']}\n"
        info += f"⚡ Energy Usage: {data['energy_use']}\n"
        info += f"🌱 Sustainability Score: {data['sustainability_score']}/10\n"
        info += f"📝 Description: {data['description']}\n"
        
        # Add investment recommendation
        if data['sustainability_score'] >= 7 and data['price_trend'] == 'rising':
            info += "\n🌟 RECOMMENDATION: Excellent choice for sustainable long-term investment!"
        elif data['price_trend'] == 'rising':
            info += "\n📈 RECOMMENDATION: Good for short-term gains, but consider environmental impact."
        elif data['sustainability_score'] >= 7:
            info += "\n🌱 RECOMMENDATION: Great for eco-conscious investors!"
        else:
            info += "\n⚠️ RECOMMENDATION: Consider other options for better returns or sustainability."
        
        return info

    def process_query(self, user_input):
        """Process user queries and provide appropriate responses"""
        user_input = user_input.lower().strip()
        
        # Help command
        if user_input in ['help', 'commands', 'what can you do']:
            return self.show_help()
        
        # Greeting responses
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            return "👋 Hello again! What crypto questions can I help you with today?"
        
        # Sustainable crypto queries
        elif any(word in user_input for word in ['sustainable', 'eco', 'green', 'environment', 'climate']):
            sustainable_coins = self.get_sustainable_cryptos()
            if sustainable_coins:
                response = "🌱 Most Sustainable Cryptocurrencies:\n"
                for i, (coin, score) in enumerate(sustainable_coins[:3], 1):
                    response += f"{i}. {coin} - Sustainability Score: {score}/10 🌟\n"
                response += "\n💡 These coins use energy-efficient consensus mechanisms!"
                return response
            else:
                return "❌ No sustainable cryptocurrencies found in my database."
        
        # Trending/profitable crypto queries
        elif any(word in user_input for word in ['trending', 'rising', 'profitable', 'gains', 'moon']):
            trending_coins = self.get_trending_cryptos()
            if trending_coins:
                response = "🚀 Trending Cryptocurrencies (Rising Price Trend):\n"
                for i, coin in enumerate(trending_coins, 1):
                    price = self.crypto_db[coin]['current_price']
                    response += f"{i}. {coin} - Current Price: ${price} 📈\n"
                response += "\n💰 These coins are showing upward momentum!"
                return response
            else:
                return "❌ No trending cryptocurrencies found."
        
        # Low energy crypto queries
        elif any(word in user_input for word in ['low energy', 'energy efficient', 'power consumption']):
            low_energy_coins = self.get_low_energy_cryptos()
            if low_energy_coins:
                response = "⚡ Energy-Efficient Cryptocurrencies:\n"
                for i, coin in enumerate(low_energy_coins, 1):
                    response += f"{i}. {coin} - Low energy consumption 🌿\n"
                return response
            else:
                return "❌ No low-energy cryptocurrencies found."
        
        # Investment advice queries
        elif any(word in user_input for word in ['invest', 'buy', 'recommend', 'advice', 'portfolio']):
            # Get best overall recommendation
            best_coin = None
            best_score = 0
            
            for coin, data in self.crypto_db.items():
                # Calculate combined score (profitability + sustainability)
                profit_score = 3 if data['price_trend'] == 'rising' else 1
                sustainability_score = data['sustainability_score']
                market_score = 3 if data['market_cap'] == 'high' else 2
                
                total_score = profit_score + sustainability_score + market_score
                
                if total_score > best_score:
                    best_score = total_score
                    best_coin = coin
            
            if best_coin:
                data = self.crypto_db[best_coin]
                response = f"🌟 INVESTMENT RECOMMENDATION: {best_coin}\n"
                response += f"💰 Price: ${data['current_price']}\n"
                response += f"📈 Trend: {data['price_trend']}\n"
                response += f"🌱 Sustainability: {data['sustainability_score']}/10\n"
                response += f"📝 {data['description']}\n"
                response += "\n⚠️ Remember: This is not financial advice! Always DYOR!"
                return response
        
        # Comparison queries
        elif 'compare' in user_input or 'vs' in user_input:
            # Extract cryptocurrency names from the query
            words = user_input.split()
            crypto_names = []
            
            # Look for cryptocurrency names in the input
            for word in words:
                for coin in self.crypto_db:
                    if coin.lower() in word.lower() or word.lower() in coin.lower():
                        if coin not in crypto_names:
                            crypto_names.append(coin)
            
            # Also check for common patterns like "bitcoin and ethereum"
            input_lower = user_input.lower()
            for coin in self.crypto_db:
                if coin.lower() in input_lower:
                    if coin not in crypto_names:
                        crypto_names.append(coin)
            
            if len(crypto_names) >= 2:
                return self.compare_cryptos(crypto_names[0], crypto_names[1])
            elif len(crypto_names) == 1:
                return f"I found {crypto_names[0]} in your query. Please specify another cryptocurrency to compare it with."
            else:
                return "📊 To compare cryptocurrencies, please specify two coins like: 'compare Bitcoin and Ethereum'"
        
        # List all cryptocurrencies
        elif any(word in user_input for word in ['list', 'all', 'available', 'show me']):
            response = "📋 Available Cryptocurrencies in my database:\n"
            for i, (coin, data) in enumerate(self.crypto_db.items(), 1):
                response += f"{i}. {coin} ({data['symbol']}) - ${data['current_price']}\n"
            response += "\n💡 Ask me about any of these cryptocurrencies!"
            return response
        
        # Specific crypto information
        else:
            # Check if user is asking about a specific cryptocurrency
            for coin in self.crypto_db:
                if coin.lower() in user_input:
                    return self.get_crypto_info(coin)
            
            # Default response for unrecognized queries
            return ("🤔 I'm not sure what you're asking about. Try asking about:\n"
                   "• Sustainable cryptocurrencies\n"
                   "• Trending/profitable coins\n"
                   "• Specific crypto information (e.g., 'tell me about Bitcoin')\n"
                   "• Investment recommendations\n"
                   "• Comparison between cryptocurrencies\n"
                   "Type 'help' for more options!")

    def show_help(self):
        """Display help information"""
        help_text = """
🆘 CryptoBuddy Help Center
========================

🔍 Available Commands:
• 'sustainable' or 'eco' - Find eco-friendly cryptocurrencies
• 'trending' or 'profitable' - Find coins with rising trends
• 'invest' or 'recommend' - Get investment recommendations
• 'compare [coin1] and [coin2]' - Compare two cryptocurrencies
• 'list' or 'all' - Show all available cryptocurrencies
• '[crypto name]' - Get detailed info about a specific coin
• 'help' - Show this help menu
• 'quit' - Exit the chatbot

💡 Example Questions:
• "What's the most sustainable crypto?"
• "Which coins are trending up?"
• "Tell me about Cardano"
• "Should I invest in Bitcoin?"
• "Compare Ethereum and Solana"

⚠️ Disclaimer: This is educational content only, not financial advice!
"""
        return help_text

    def run(self):
        """Main chatbot loop"""
        self.greet()
        
        while True:
            try:
                user_input = input("🗣️ You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n{random.choice(self.farewells)}")
                    break
                
                if not user_input:
                    print("💬 Please ask me something about cryptocurrencies!")
                    continue
                
                # Simulate processing time
                print("🤖 CryptoBuddy is thinking...")
                time.sleep(1)
                
                response = self.process_query(user_input)
                print(f"\n🤖 CryptoBuddy: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{random.choice(self.farewells)}")
                break
            except Exception as e:
                print(f"❌ Oops! Something went wrong: {e}")
                print("🔄 Let's try again!")

# Additional utility functions for advanced features
def simulate_market_update():
    """Simulate real-time market updates (for demonstration)"""
    print("📊 Market Update Simulation:")
    print("• Bitcoin: +2.5% (24h)")
    print("• Ethereum: -1.2% (24h)")
    print("• Cardano: +5.7% (24h)")
    print("• Solana: +3.1% (24h)")

def risk_disclaimer():
    """Display investment risk disclaimer"""
    disclaimer = """
⚠️ IMPORTANT DISCLAIMER:
• Cryptocurrency investments are highly volatile and risky
• Past performance does not guarantee future results
• Only invest what you can afford to lose
• This chatbot provides educational information, not financial advice
• Always do your own research (DYOR) before investing
• Consider consulting with a financial advisor
"""
    return disclaimer

# Main execution
if __name__ == "__main__":
    print("🚀 Welcome to CryptoBuddy - Your AI-Powered Financial Sidekick!")
    print(risk_disclaimer())
    
    # Initialize and run the chatbot
    crypto_buddy = CryptoBuddy()
    crypto_buddy.run()
