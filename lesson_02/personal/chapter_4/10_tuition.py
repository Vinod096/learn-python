#At one college, the tuition for a full-time student is $8,000 per semester. It has been
#announced that the tuition will increase by 3 percent each year for the next 5 years. Write
#a program with a loop that displays the projected semester tuition amount for the next 5
#years.

tuition_fee_per_sem = 8000
percent_of_fee_hike = 0.03
years = 5
for years in range (1,6):
    tuition_fee_per_sem = tuition_fee_per_sem + (tuition_fee_per_sem * percent_of_fee_hike)
    print(f"fee for {years} year : {tuition_fee_per_sem}")
