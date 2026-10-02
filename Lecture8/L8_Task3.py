words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}

for w in words:
    if w in word_counts:
        word_counts[w] += 1 
    else:
        word_counts[w] = 1 

print(word_counts)

for word, count in word_counts.items():
    if count > 1:
        print(word)