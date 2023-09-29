import re  # We're using a tool to work with patterns of text.

# Sample HTML code containing web links
html_code = """
<p>Visit our website <a href="<https://www.example.com>">Example Website</a></p>
<p>Explore more at <a href="<http://subdomain.example.co.uk>">Subdomain</a></p>
<p>Check out our products <a href="<https://www.productstore.com/products>">Product Store</a></p>
"""

# Define a pattern to find web links in HTML
# This pattern looks for parts of the code that look like links.
reg_exp = r'<a[^>]*href="([^"]+)"[^>]*>'

# Find all web links in the HTML using the pattern
hyperlinks = re.findall(reg_exp, html_code)

# Print the found web links
for hyperlink in hyperlinks:
    print(hyperlink)  # We're showing the links we found.
