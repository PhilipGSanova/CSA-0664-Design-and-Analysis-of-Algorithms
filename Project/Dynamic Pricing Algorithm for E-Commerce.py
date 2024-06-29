import numpy as np

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
    
    return dp, prices

# Example usage
products = ['A', 'B', 'C']
periods = 10
base_demand = [100, 80, 60]  # Example base demand for products
elasticity = [-1.2, -1.5, -1.3]  # Example demand elasticity for products
initial_inventory = [500, 400, 300]  # Example initial inventory levels
competitor_prices = np.random.rand(len(products), periods) * 100  # Random competitor prices

# Run the dynamic pricing algorithm
revenues, optimal_prices = dynamic_pricing(products, periods, base_demand, elasticity, initial_inventory, competitor_prices)

# Print results
print("Optimal Prices:\n", optimal_prices)
print("Revenues:\n", revenues)
