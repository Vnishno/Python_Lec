scores = []
# scores.extend([45, 88, 92, 60, 75])

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

scores.remove(45)

print(sum(scores)/len(scores))
print(max(scores))
print(min(scores))

scores.sort()
print(scores)

passed_score = [x for x in scores if x >= 60 ]
print(passed_score)