numbers = [7,10,30,20,40]
numbers_2 = [50,60,70]
numbers.extend(numbers_2)
print(numbers)

print("**********append**********")

numbers.append(80)
print(numbers)

print("**********clear**********")

numbers_2.clear()
print(numbers_2)

print("**********remove**********")

numbers.remove(70)
print(numbers)

print("**********pop**********")

numbers.pop(2)
print(numbers)

print("**********reverse**********")

numbers.reverse()
print(numbers)

print("**********sort**********")

numbers.sort()
print(numbers)

print("**********count**********")
names = ['alena', 'adeev', 'aleev']
x = names.count('aleev')
print(x)

