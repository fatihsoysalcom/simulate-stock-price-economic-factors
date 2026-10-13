import random
import math

def simulate_stock_price():
    """
    Simulates a stock price over time, influenced by hypothetical economic factors.
    This example demonstrates how various factors (like semiconductor demand,
    global sentiment, and interest rates) can impact a stock's value,
    reflecting the concepts discussed in the article about Kospi and SK Hynix.
    """
    INITIAL_PRICE = 100.0  # Starting price for the simulated stock
    DAYS_TO_SIMULATE = 60  # Simulate for 60 trading days (approx 3 months)
    BASE_VOLATILITY = 0.015 # Base daily fluctuation percentage

    # Initial values for hypothetical economic indicators
    # These are simplified representations of complex market dynamics.
    semiconductor_demand_index = 1.0 # 1.0 means normal demand
    global_economic_sentiment = 1.0  # 1.0 means neutral sentiment
    interest_rate_impact = 0.0       # 0.0 means no negative impact from rates

    current_price = INITIAL_PRICE
    price_history = []

    print(f"Simulating Stock Price Fluctuations over {DAYS_TO_SIMULATE} days")
    print("-" * 60)
    print(f"{'Day':<5} {'Price':<10} {'Demand':<10} {'Sentiment':<10} {'Rates':<10} {'Chart':<20}")
    print("-" * 60)

    for day in range(1, DAYS_TO_SIMULATE + 1):
        # Simulate changes in economic factors over time
        # These changes are simplified and illustrative, designed to show a downturn.
        if day < 20:
            # Initial stable period
            semiconductor_demand_index += random.uniform(-0.001, 0.002)
            global_economic_sentiment += random.uniform(-0.001, 0.001)
        elif 20 <= day < 40:
            # Simulate a downturn in demand and sentiment, and rising rates
            semiconductor_demand_index -= random.uniform(0.005, 0.01) # Demand drops, reflecting 'arz-talep dengesizlikleri'
            global_economic_sentiment -= random.uniform(0.003, 0.007) # Sentiment worsens, reflecting 'küresel piyasalar'
            interest_rate_impact += random.uniform(00.001, 0.003)      # Rates rise, increasing negative impact, reflecting 'faiz artırım politikaları'
        else:
            # Stabilize or slight recovery/continued pressure
            semiconductor_demand_index += random.uniform(-0.002, 0.003)
            global_economic_sentiment += random.uniform(-0.002, 0.002)
            interest_rate_impact -= random.uniform(0.0005, 0.0015) # Rates impact might lessen or stabilize

        # Ensure factors don't go too far out of bounds for realism
        semiconductor_demand_index = max(0.7, min(1.2, semiconductor_demand_index))
        global_economic_sentiment = max(0.6, min(1.1, global_economic_sentiment))
        interest_rate_impact = max(0.0, min(0.05, interest_rate_impact)) # Max 5% negative impact

        # Calculate daily price change based on volatility and economic factors
        # The core idea is that economic factors modify the expected daily return.
        daily_volatility = random.gauss(0, BASE_VOLATILITY)

        # Influence from semiconductor demand: higher demand -> positive impact
        demand_influence = (semiconductor_demand_index - 1.0) * 0.05

        # Influence from global economic sentiment: positive sentiment -> positive impact
        sentiment_influence = (global_economic_sentiment - 1.0) * 0.03

        # Influence from interest rates: higher impact -> negative influence
        rates_influence = -interest_rate_impact * 0.5 # Negative multiplier, simulating 'yüksek faiz oranları'

        # Combine influences to get an adjusted daily return expectation
        # This simulates how market news (like those in the article) can shift price.
        total_influence = demand_influence + sentiment_influence + rates_influence

        # Apply the total influence and volatility to the price
        # Using exponential for more realistic price changes
        daily_return = math.exp(daily_volatility + total_influence) - 1
        current_price *= (1 + daily_return)

        price_history.append(current_price)

        # Simple text-based chart
        chart_bar = '#' * int((current_price / INITIAL_PRICE) * 10)
        chart_display = f"[{chart_bar:<10}]"

        print(f"{day:<5} {current_price:<10.2f} {semiconductor_demand_index:<10.2f} {global_economic_sentiment:<10.2f} {interest_rate_impact:<10.2f} {chart_display}")

    print("-" * 60)
    print(f"Simulation complete. Final price: {current_price:.2f}")
    if current_price < INITIAL_PRICE:
        print(f"The simulated stock experienced a decline of {((INITIAL_PRICE - current_price) / INITIAL_PRICE) * 100:.2f}%")
    else:
        print(f"The simulated stock experienced a gain of {((current_price - INITIAL_PRICE) / INITIAL_PRICE) * 100:.2f}%")

if __name__ == "__main__":
    simulate_stock_price()
