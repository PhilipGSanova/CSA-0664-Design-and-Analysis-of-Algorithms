import numpy as np
import matplotlib.pyplot as plt

def demand(price, base_demand, elasticity):
    if price == 0 and elasticity < 0:
        return 0
    return base_demand * (price ** elasticity)

def dynamic_pricing(products, periods, base_demand, elasticity, initial_inventory, competitor_prices):
    # Initialize the DP table, prices, and inventory
    dp = np.zeros((len(products), periods))
    prices = np.zeros((len(products), periods))
    inventory = np.zeros((len(products), periods))
    
    # Iterate over each period
    for t in range(periods):
        for i, product in enumerate(products):
            max_revenue = 0
            best_price = 0
            
            # Iterate over a range of possible prices (1 to 100 as an example)
            for price in np.linspace(1, 100, 100):
                current_demand = demand(price, base_demand[i], elasticity[i])
                current_inventory = initial_inventory[i] if t == 0 else inventory[i][t-1]
                
                # Skip if demand exceeds current inventory
                if current_demand > current_inventory:
                    continue
                
                revenue = price * current_demand
                
                # Add revenue from the previous period if not the first period
                if t > 0:
                    revenue += dp[i][t-1]
                
                # Update maximum revenue and best price
                if revenue > max_revenue:
                    max_revenue = revenue
                    best_price = price
            
            # Update DP table, optimal prices, and inventory
            dp[i][t] = max_revenue
            prices[i][t] = best_price
            inventory[i][t] = current_inventory - demand(best_price, base_demand[i], elasticity[i])
    
    return dp, prices, inventory

def static_pricing(products, periods, base_demand, elasticity, initial_inventory, competitor_prices, static_price, inventory):
    # Initialize arrays to store revenue
    static_revenue = np.zeros(periods)
    
    # Iterate over each period
    for t in range(periods):
        for i, product in enumerate(products):
            price = static_price[i]
            current_demand = demand(price, base_demand[i], elasticity[i])
            current_inventory = initial_inventory[i] if t == 0 else inventory[i][t-1]
            
            # Skip if demand exceeds current inventory
            if current_demand > current_inventory:
                continue
            
            revenue = price * current_demand
            
            # Add revenue from the previous period if not the first period
            if t > 0:
                revenue += static_revenue[t-1]
            
            # Update revenue for the current period
            static_revenue[t] += revenue
    
    return static_revenue

# Example usage and comparison
products = ['A', 'B', 'C']
periods = 10
base_demand = [100, 80, 60]  # Example base demand for products
elasticity = [-1.2, -1.5, -1.3]  # Example demand elasticity for products
initial_inventory = [500, 400, 300]  # Example initial inventory levels
competitor_prices = np.random.rand(len(products), periods) * 100  # Random competitor prices
static_prices = [50, 60, 70]  # Example static prices for comparison

# Run dynamic pricing algorithm
dynamic_revenues, dynamic_optimal_prices, dynamic_inventory = dynamic_pricing(products, periods, base_demand, elasticity, initial_inventory, competitor_prices)

# Run static pricing strategy
static_revenues = static_pricing(products, periods, base_demand, elasticity, initial_inventory, competitor_prices, static_prices, dynamic_inventory)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, periods + 1), dynamic_revenues.sum(axis=0), marker='o', linestyle='-', color='b', label='Dynamic Pricing')
plt.plot(np.arange(1, periods + 1), static_revenues, marker='s', linestyle='--', color='r', label='Static Pricing')
plt.xlabel('Periods')
plt.ylabel('Total Revenue')
plt.title('Comparison of Dynamic Pricing vs Static Pricing')
plt.xticks(np.arange(1, periods + 1))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
