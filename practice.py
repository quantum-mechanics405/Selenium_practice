import numpy as np

love_words = np.array([
    "affection",
    "adore",
    "cherish"
])

# Randomly select one word with replacement

for _ in range(10):
    random_word = np.random.choice(love_words)
    print(random_word)
