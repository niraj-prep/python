import pandas as pd
import os

def create_sample_csv():
    data = {
        "Title": [
            "Python Crash Course",
            "Learning Python",
            "Clean Code",
            "The Pragmatic Programmer",
            "Data Science Handbook",
            "Automate the Boring Stuff",
            "Fluent Python",
            "Effective Java",
        ],
        "Author": [
            "Eric Matthes",
            "Mark Lutz",
            "Robert C. Martin",
            "Andrew Hunt",
            "Jake VanderPlas",
            "Eric Matthes",
            "Luciano Ramalho",
            "Joshua Bloch",
        ],
        "Edition": [2, 5, 1, 2, 1, 2, 2, 3],
        "Publication_Year": [2019, 2013, 2008, 2019, 2016, 2020, 2022, 2018],
        "Publishing_House": [
            "No Starch Press",
            "O'Reilly",
            "Prentice Hall",
            "Addison-Wesley",
            "O'Reilly",
            "No Starch Press",
            "O'Reilly",
            "Addison-Wesley",
        ],
        "Price": [350, 750, 499, 620, 580, 299, 680, 540],
    }
    df = pd.DataFrame(data)
    df.to_csv("books.csv", index=False)
    print("✔  books.csv created successfully.\n")


if not os.path.exists("books.csv"):
    create_sample_csv()

df = pd.read_csv("books.csv")

print("=" * 70)
print("  a) Complete Report of Books")
print("=" * 70)
print(df.to_string(index=False))
print()

print("=" * 70)
print("  b) Books by a Given Author")
print("=" * 70)
author_name = "Eric Matthes"          # ← change as needed
author_books = df[df["Author"] == author_name]
if author_books.empty:
    print(f"  No books found for author: {author_name}")
else:
    print(f"  Author: {author_name}")
    print(author_books[["Title", "Edition", "Publication_Year", "Price"]].to_string(index=False))
print()

print("=" * 70)
print("  c) Books by a Given Publishing House")
print("=" * 70)
pub_house = "O'Reilly"                # ← change as needed
pub_books = df[df["Publishing_House"] == pub_house]
if pub_books.empty:
    print(f"  No books found for publisher: {pub_house}")
else:
    print(f"  Publisher: {pub_house}")
    print(pub_books[["Title", "Author", "Edition", "Price"]].to_string(index=False))
print()

print("=" * 70)
print("  d) Cheapest & Costliest Books")
print("=" * 70)
cheapest = df.loc[df["Price"].idxmin()]
costliest = df.loc[df["Price"].idxmax()]
print(f"  Cheapest  Book : '{cheapest['Title']}'  — ₹{cheapest['Price']}")
print(f"  Costliest Book : '{costliest['Title']}'  — ₹{costliest['Price']}")
print()


print("=" * 70)
print("  e) Books Sorted by Year of Publication")
print("=" * 70)
sorted_df = df.sort_values("Publication_Year")
print(sorted_df[["Title", "Author", "Publication_Year", "Price"]].to_string(index=False))
print()