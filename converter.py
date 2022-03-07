# Python program to convert
# CSV to HTML Table


import pandas as pd

# to read csv file named "samplee"
a = pd.read_csv("poinst.csv")

# to save as html file
# named as "Table"
a.to_html("index.htm")

# assign it to a
# variable (string)
html_file = a.to_html()