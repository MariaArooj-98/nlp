# A List is a collection which is ordered and changeable. Allows duplicate members.
import re

# Sample CSS stylesheet
css_stylesheet = """
body {
    background-color: #FFAABB;
    color: #00FF00;
}

.header {
    background: url('image.png');
    border: 1px solid #123456;
}
"""

# Regular expression pattern to extract hexadecimal color codes
color_code_pattern = r'#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})'

# Find all color codes using the regular expression
color_codes = re.findall(color_code_pattern, css_stylesheet)

# Print the extracted color codes
for color_code in color_codes:
    print(color_code)
