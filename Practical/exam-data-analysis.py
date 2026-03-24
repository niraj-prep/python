import pandas as pd
import numpy as np

exam_data = {
    'name': ['Ajay', 'Vijay', 'Vivek', 'Atharv', 'Apurva', 'Rupal', 'Priyal', 'Shrushti', 'Vishal', 'Pranay'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

	# write your code here...
df=pd.DataFrame(exam_data, index=labels)
def select_name_score(df):
	return df[['name','score']]
def select_score_range(df):
	return df[df['score'].between(15,20)]
def select_missing_scores(df):
	return df[df['score'].isna()]
def update_score_d(df):
	df.loc['d','score']=11.5
	return df
def total_attempts(df):
	return df['attempts'].sum()

print("Original DataFrame:")
print(df)

print("Selected 'name' and 'score' columns:")
print(select_name_score(df))

print("Rows with scores between 15 and 20:")
print(select_score_range(df))

print("Rows with missing scores:")
print(select_missing_scores(df))

print("DataFrame after updating score in row 'd' to 11.5:")
df_updated = update_score_d(df.copy())
print(df_updated)

print("Total attempts by all students:")
print(total_attempts(df))