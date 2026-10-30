def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C" 
    elif score >= 60:
        return "D" 
    else:
        return "F" 

scores = [88, 92, 79, 65, 95, 70, 84]

for score in scores:
    print(f"{score}: {letter_grade(score)}")

