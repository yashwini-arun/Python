# Assignment/main_utils.py
from .csv_parser import read_csv, write_csv
from .word_counter import count_words, top_n_words




def main():
    # Example 1: CSV usage
    rows = [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
    ]
    write_csv("Assignment/people.csv", fieldnames=["Name", "Age"], rows=rows)
    print("✅ CSV Written")

    data = read_csv("Assignment/people.csv")
    print("📂 CSV Read:", data)

    # Example 2: Word Counter
    text = "Python is simple. Python is powerful. I love Python!"
    print("📝 Word counts:", count_words(text))
    print("🔥 Top 3 words:", top_n_words(text, 3))

if __name__ == "__main__":
    main()
