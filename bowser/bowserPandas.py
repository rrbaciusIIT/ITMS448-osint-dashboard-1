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
print(f"{true_count_hate} \t Contains Consipracy Theories")



import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()