# Dictionaries
# Lists
# Tuples
# Sets

age = [1,2,3,4,5,1,1,1,2,2,2]
ages_1 = {"1": 23, "2":33, "3":43, "10":12,"5":4}
ages_2 = {1: 23, 2:33, 3:43}

print(ages_1["5"])
print(ages_2[2])

#print(days)

ages = set((1, 2, 3, 4, 5, 1, 1, 1, 2, 2, 2))
print(ages)

for age in ages:
    print(age)


tup = (1,2,3,4,4,2,1)
lis = [1,2,3,4,4,2,1]

lis[0] = 7 #Mutable
# tup[0] = 6 #Immutable

print(lis)
print(tup)

print(set(lis))
print(set(tup))
