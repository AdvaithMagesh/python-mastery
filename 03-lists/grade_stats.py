scores = [88, 92, 79, 65, 95, 70, 84]
average = sum(scores)/len(scores)
highest = max(scores)
lowest = min(scores)

print(f"The average is {average:.1f}")
print(f"The highest score was {highest}")
print(f"The lowest score was {lowest}")

count_80_plus = 0

for score in scores:
    if score >= 80:
        count_80_plus += 1

print(f"There are {count_80_plus} scores 80 or above in the list!")

print(sorted(scores, reverse=True))

