# A function that reads a given file and the lists the words and their correspoding frequencies

import re
from collections import Counter

def count(file):
    with open(file,'r') as file:
        data = file.read().lower()

        pattern = r"\b\w+\b"

        words = re.findall(pattern,data)
        print(words)

        length = len(words)
        print(length)

        frequency = Counter(words)

        sorted_words = sorted(frequency.items(), key = lambda x:x[1])
        print(sorted_words)

        for word, count in sorted_words:
            print(f"{word}: {count}")

        
count('demo.txt')