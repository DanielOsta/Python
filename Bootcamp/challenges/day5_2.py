student_heights = input("Heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


sum = 0
length = 0
for height in student_heights:
    sum += height
    length += 1

avg = round(sum / length)

print(avg)

print("Max height: " + str(max(student_heights)))
