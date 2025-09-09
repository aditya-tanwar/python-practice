

# AND/and conditional

score = int(input("Enter your score : "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("grade: B")
else:
    print("Grade: C")
    
    
# this can also be written as <condition>.<variable / subject>.<condition>

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
else:
    print("C")