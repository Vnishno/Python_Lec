scores = [45, 82, 67, 38, 90, 55, 72]

passing_scores = list(filter(lambda x: x >= 50, scores))
updated_scores = list(map(lambda x: min(x + 5, 100), passing_scores))

print(updated_scores)