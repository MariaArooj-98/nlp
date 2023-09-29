import re  # We're using a tool for working with text patterns.

# Sample text containing the word "Apple"
text = "I love Apple. The Apple company is doing well. Apple pie is delicious."

# Define regular expressions for identifying "Apple" as a fruit and as a company
fruit_pattern = r'\bApple\b(?!\s+Inc\.| company)'

company_pattern = r'\bApple\b\s+(Inc\.|company)'


# Find matches for both patterns in the text
fruit_matches = re.findall(fruit_pattern, text)
company_matches = re.findall(company_pattern, text)

# Determine the context and disambiguate
for match in fruit_matches:
    print(f'Found "Apple" as a fruit: {match}')

for match in company_matches:
    print(f'Found "Apple" as a company: {match}')
