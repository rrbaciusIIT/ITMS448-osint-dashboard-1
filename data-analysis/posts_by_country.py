import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series

df = pd.read_csv('../bowser/out/post-output-large.csv')

country_code_counts: Series = df['country_code'].value_counts()

# Remove all country code entries that happen less than a certain number of times
for countrycode, count in country_code_counts.items():
	if count < 50:
		country_code_counts = country_code_counts.drop(countrycode)

plt.pie(country_code_counts.values, labels=list(country_code_counts.keys()))
plt.title("Post amount by country code")
plt.legend(country_code_counts.values, loc=3)
plt.show()
