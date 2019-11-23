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



df = pd.DataFrame({'count': [true_count_racist,true_count_hate]})
plot = df.plot.pie(y='count',figsize=(5,5))