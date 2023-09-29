import re  # We're using a tool for working with text patterns.

# Sample text containing addresses
text = """
123 Main St, Apt 4B
456 Elm Avenue
789 Oak St, Suite 101
1011 Willow Rd
"""

# Regular expression to extract street addresses
address_pattern = r'\b\d+\s+[A-Za-z]+\s+(?:\w+\s+)?\d*[A-Za-z]*\b'
# Find all addresses using the regular expression
addresses = re.findall(address_pattern, text)

# Print the extracted addresses
for address in addresses:
    print(address)  # Display each extracted street address.
