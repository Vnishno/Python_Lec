def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = []

    words = text.split()
    count = 0
    for i in words:
        # ამოწმებთ კონკრეტულ სიტყვას (i) და არა სიას (words)
        if len(i) >= min_length and i not in ignore_stopwords: 
            count += 1
    return count

text1 = "Hello Python I am Giorgi"

print(analyze_text(text1))

print(analyze_text(text1, ignore_stopwords=["Hello"]))
