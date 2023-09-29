# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

import re

# Sample sample document containing dates in different formats
sample = """
Date 1: 09/25/2023
Date 2: 2023-12-15
Date 3: 05-20-2022
Date 4: 2022/06/30
"""

# Define a regular expression pattern to match various date formats
pattern = r"\\b(\\d{4}[-/]\\d{2}[-/]\\d{2}|\\d{2}[-/]\\d{2}[-/]\\d{4})\\b"

# Function to format matched dates
def format_date(match):
    date = match.group(0)
    # Replace "-" or "/" with "/"
    date = re.sub(r"[-/]", "/", date)
    # Split the date using "/" and reformat it to "YYYY/MM/DD" format
    parts = date.split("/")
    formatted_date = f"{parts[2]}/{parts[0].zfill(2)}/{parts[1].zfill(2)}"
    return formatted_date

# Find all dates using the regular expression
dates = re.findall(pattern, sample)

# Replace the original dates with the formatted dates
formatted_sample = re.sub(pattern, format_date, sample)

# Print the formatted sample
print(formatted_sample)
