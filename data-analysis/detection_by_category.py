from typing import List

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../bowser/out/post-output-large.csv')

# List of header names, i.e. [board, postid, posturl]
column_headers: List[str] = list(df.head().keys())

# List of header names that have to do with content flagger analyses.
# Notice the filters can be changed with boolean operators
column_headers_content_flagger: List[str] = list(filter(
	lambda x: (
			(('[content flagger]' in x) and
			 ('PRISM' not in x) and  # Don't use PRISM or ECHELON: They kind of suck currently.
			 ('ECHELON' not in x))  # Extremely high false positive rate.
			or
			('No content flagger tripped' in x)  # include that stat that tells us if no content flagger was tripped
	),
	column_headers))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list(map(
	lambda x: x.replace('[content flagger]', ''),  # remove those ugly labels
	column_headers_content_flagger))

values = [df[header].sum() for header in column_headers_content_flagger]

plt.pie(values, labels=values)
plt.title("Detection breakdown by category, with benign posts")
plt.legend(labels, loc=10)
plt.show()
