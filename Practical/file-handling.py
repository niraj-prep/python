from collections import Counter
import os


def read_file():
    # write your code here...
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print("File not found")


def write_names():
    # write your code here...
    filename = input("Enter the filename: ")
    names = input("Enter comma-separated names: ").split(',')
    with open(filename, "w") as file:
        for name in names:
            file.write(name.strip())
    print("Names written to file")


def count_words():
    # write your code here...
    src = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    try:
        with open(src, "r") as file:
            words = file.read().lower().split()
        words_counts = Counter(words)
        with open(output_file, "w") as file:
            for word, count in words_counts.items():
                file.write(f"{word}:{count}")
        print(f"Word counts written to '{output_file}'.")
    except FileNotFoundError:
        print("Input file not found")


def file_mode_demo():
    # write your code here...
    with open('demo.txt', 'w') as f:
        f.write("Line written using 'w' mode")
    with open('demo.txt', 'a') as f:
        f.write("Line appended using 'a' mode")
    try:
        with open('demo.txt', 'r') as f:
            print("Content after 'r' mode:")
            print(f.read())
    except FileNotFoundError:
        print("demo.txt not found")

    try:
        with open('demo.txt', 'r+') as f:
            original = f.read()
            f.seek(0)
            f.write("Modified using 'r+' mode")
            print("Content before 'r+' modification:")
            print(original)
    except FileNotFoundError:
        print("demo.txt not found")


def main():
    while True:
        print("1. Read a file")
        print("2. Write names to a file")
        print("3. Count words and write to another file")
        print("4. Demonstrate file modes")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            read_file()
        elif choice == '2':
            write_names()
        elif choice == '3':
            count_words()
        elif choice == '4':
            file_mode_demo()
        elif choice == '5':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()