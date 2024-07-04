# Calculate average temperature


numDays = int(input("How many days temperature? "))
total = 0
temp = []

for i in range(numDays):
    nextDay = int(input("Day " + str(i) + "'s high temperature: "))
    temp.append(nextDay)
    total += temp[i]

average_temp = round(total / numDays, 2)

print("\nAverage = " + str(average_temp))

above = 0
for i in temp:
    if i > average_temp:
        above += 1

print(str(above) + " day(s) above average")
