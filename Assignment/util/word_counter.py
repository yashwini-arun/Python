# Assignment/utils/word_counter.py
from collections import Counter
import re

def count_words(text):
    """Return a dictionary with word counts from a string."""
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))

def top_n_words(text, n=5):
    """Return the n most common words."""
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words).most_common(n)
