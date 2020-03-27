#Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
#application that displays the number of millimeters that the ocean will have risen each year
#for the next 25 years.

rising_oceans_levels_per_year = 1.6
years = 0
for i in range (1,26):
    years = rising_oceans_levels_per_year * i
    print(f"rising levels per {i} year : {years}")
