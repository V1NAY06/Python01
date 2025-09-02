marks = []
for i in range(6):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

marks.sort()
print("Sorted marks:", marks)
