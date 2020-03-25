#Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8.
#Write a program that calculates the number of packages of hot dogs and the number of
#packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.
#The program should ask the user for the number of people attending the cookout and the
#number of hot dogs each person will be given. The program should display the following
#details:
#• The minimum number of packages of hot dogs required
#• The minimum number of packages of hot dog buns required
#• The number of hot dogs that will be left over
#• The number of hot dog buns that will be left over

hot_dogs_packt = 10
hot_dogs_buns_packt = 8
people_attending = int(input("enter the number of people attending : "))
hot_dog_for_each_person = int(input("enter the number of hot dogs for each person :"))
minimum_number_of_hot_dogs_required = people_attending * hot_dog_for_each_person
print("minimum hot dogs required :",minimum_number_of_hot_dogs_required)
minimum_number_of_hot_dog_buns_required = people_attending * hot_dog_for_each_person
print("minimum number of packages of hot dog buns required :",minimum_number_of_hot_dog_buns_required)
leftovers_hot_dogs = minimum_number_of_hot_dogs_required % hot_dogs_packt
print("hot dogs left over are :",leftovers_hot_dogs)
leftovers_hot_dogs_buns = minimum_number_of_hot_dog_buns_required % hot_dogs_buns_packt
print("hot dogs left over are :", leftovers_hot_dogs_buns)
