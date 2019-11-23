import pandas as pd
df = pd.read_csv('out/post-output-large.csv')
unique_post = df.post_id.nunique()
print(f"{unique_post} \t\tTotal Unique Posts Found")


total_comments = df.thread_id.sum()
print(f"{total_comments} \tTotal Comments made")


print('\n\nDisplaying total flagged comments')

#true_count_bad_language = df.has_bad_language_content.sum()
#print(f"{true_count_bad_language} \t Contains bad language")

true_count_racist = df["[content flagger] Contains racism"].sum()
print(f"{true_count_racist} \t Contains Racism ")

true_count_hate = df["[content flagger] Contains hate speech"].sum()
print(f"{true_count_hate} \t Contains Hate Speech")

true_count_terrorism = df["[content flagger] Contains terrorist language"].sum()
print(f"{true_count_terrorism} \t Contains Terrorist Language")

true_count_PRISM = df["[content flagger] Contains keywords that may trigger NSA PRISM filters"].sum()
print(f"{true_count_PRISM} \t Contains NSA PRISM Keywords")

true_count_conspiracy = df["[content flagger] Contains conspiracy theories"].sum()
print(f"{true_count_conspiracy} \t Contains Consipracy Theories")

true_count_ECHELON = df["[content flagger] Contains keywords that may trigger NSA ECHELON filters"].sum()
print(f"{true_count_ECHELON} \t  Contains NSA ECHELON keywords")







import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Hate Speech', 'Racism', 'Terrorism', 'Conspiracy','PRISM','ECHELON'
Flagged = [true_count_hate, true_count_racist,true_count_terrorism, true_count_conspiracy, true_count_PRISM, true_count_ECHELON]
explode = [0, 0, 0, 0, 0.01, 0.01]

fig1, ax1 = plt.subplots()
ax1.pie(Flagged, explode=explode, labels=labels, autopct='%1.1f%%', startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()