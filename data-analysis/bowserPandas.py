import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../bowser/out/post-output-large.csv')
unique_post = df.post_id.nunique()
print(f"{unique_post} \t\tTotal Unique Posts Found")

total_comments = df.thread_id.sum()
print(f"{total_comments} \tTotal Comments made")

print('\n\nDisplaying total flagged comments')

# true_count_bad_language = df.has_bad_language_content.sum()
# print(f"{true_count_bad_language} \t Contains bad language")

true_count_racist = df["[content flagger] Contains racism"].sum()
print(f"{true_count_racist} \t Contains Racism ")

true_count_hate = df["[content flagger] Contains hate speech"].sum()
print(f"{true_count_hate} \t Contains Consipracy Theories")

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Hate Speech', 'Racism'
Flagged = [true_count_hate, true_count_racist]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(Flagged, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
