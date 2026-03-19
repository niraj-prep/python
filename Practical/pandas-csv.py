import pandas as pd
# Load the dataset
df = pd.read_csv("cars_dataset.csv")

# a) Print the first and last five rows
print("First five rows:")
print(df.head())
print("Last five rows:")
print(df.tail())

# b) Clean the dataset and update the CSV file
# Remove duplicates and rows with any null values
cleaned_df = df.drop_duplicates()
cleaned_df = cleaned_df.dropna()
cleaned_df.to_csv("cars_dataset_cleaned.csv",index=False)
print("Cleaned dataset saved as 'cars_dataset_cleaned.csv'")

# c) Find the most expensive car company name
most_expensive = cleaned_df.loc[cleaned_df["price"].idxmax()]
print(f"Most expensive car company: {most_expensive['company']}")
print(f"Car Name: {most_expensive['car_model']} | Price: {most_expensive['price']}")

# d) Print all Toyota car details
toyota_cars = cleaned_df[cleaned_df["company"].str.lower()=="toyota"]
print("All Toyota car details:")
print(toyota_cars)

# e) Count total cars per company
car_counts = cleaned_df["company"].value_counts()

print("Total cars per company:")
print(car_counts)