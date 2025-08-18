from collections import Counter
import re

def word_frequency_counter(filename):
    try:
        # Open and read the file
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        # Use regex to extract words (ignoring punctuation)
        words = re.findall(r"\b\w+\b", text)

        # Count frequencies
        word_counts = Counter(words)

        # Get top 10 words
        top_10 = word_counts.most_common(10)

        print("Top 10 most frequent words:")
        for word, freq in top_10:
            print(f"{word}: {freq}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# 🔹 Change 'sample.txt' to your text file name
word_frequency_counter("Assignments/sample.txt")

