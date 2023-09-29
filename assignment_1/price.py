import re  # Import the regular expressions module

# Sample product descriptions containing prices in various currency formats
sample_text = [
    "This product costs $100, and it's on sale for $75.",
    "Get this amazing item for just €50 or ¥5000.",
    "Price: £75.99 - limited time offer!",
    "Save 25% on your purchase ($25 off).",
]

# Define a regular expression pattern to find prices in various currency formats
price_reg_exp = r"([€$£¥]\d+(?:\.\d{2})?)"  # This pattern looks for currency symbols followed by numbers (with an optional decimal point and two digits)

# Initialize an empty list to collect the extracted prices
prices = []

# Loop through the sample_text and use the regular expression to find prices
for desc in sample_text:
    matches = re.findall(price_reg_exp, desc)  # Use regular expression to find prices in each description
    prices.extend(matches)  # Add the found prices to the 'prices' list

# Print the extracted prices
for price in prices:
    print("Prices :",price)  # Print each extracted price

