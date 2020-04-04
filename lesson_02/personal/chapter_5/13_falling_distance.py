#When an object is falling because of gravity, the following formula can be used to determine
#the distance the object falls in a specific time period:
#d = 1/2 gt 2
#The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
#amount of time, in seconds, that the object has been falling.
#Write a function named falling_distance that accepts an object’s falling time(in seconds)
#as an argument. The function should return the distance, in meters, that the object
#has fallen during that time interval. Write a program that calls the function in a loop that
#passes the values 1 through 10 as arguments and displays the return value.

def falling_distance():
    gravity = 9.8
    time = int(float(input("amount of time : ")))
    print("time"  '\t' "distance")
    for time in range(1, time + 1):
        distance = 1/2 * (gravity*time) * (gravity*time)
        print(time, '\t',distance)
    return distance

def main():
    meters = falling_distance()
    print(f"total falling distance is {meters} meters")

main()
