def calculate_shipping_cost(weight, distance, rate_per_kg, base_cost):
    """
    Calculate the shipping cost based on weight, distance, rate per kg, and base cost.

    :param weight: Weight of the package (in kg)
    :param distance: Distance to cover (in km)
    :param rate_per_kg: Rate per kg (in euros)
    :param base_cost: Base cost (in euros)
    :return: Total shipping cost (in euros)
    """
    total_cost = base_cost + (weight * rate_per_kg * distance)
    return total_cost

# file, replacing <EricMassa99>
print("Module loaded by EricMassa99")

# Example of using the function
weight = 5.0  # Weight in kg
distance = 150.0  # Distance in km
rate_per_kg = 0.1  # Rate per kg per km in euros
base_cost = 2.0  # Base cost in euros

# Calculate the shipping cost
shipping_cost = calculate_shipping_cost(weight, distance, rate_per_kg, base_cost)
print(f"The total shipping cost is: {shipping_cost:.2f} euros")
