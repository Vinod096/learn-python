#In physics, an object that is in motion is said to have kinetic energy. The following formula
#can be used to determine a moving object’s kinetic energy:
#KE = 1/2 mv2
#The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass
#in kilograms, and v is the object’s velocity in meters per second.
#Write a function named kinetic_energy that accepts an object’s mass(in kilograms) and
#velocity(in meters per second) as arguments. The function should return the amount of
#kinetic energy that the object has. Write a program that asks the user to enter values for
#mass and velocity, and then calls the kinetic_energy function to get the object’s kinetic
#energy.

def kinetic_energy():
    mass = int(float(input("Enter mass (in kilograms) : ")))
    velocity = int(float(input("Enter velocity (meters) : ")))
    k_energy = 1/2 * (mass * velocity) * (mass * velocity)
    return k_energy

def main():
    Kinetic_Energy = kinetic_energy()
    print("object’s kinetic energy :",Kinetic_Energy)

main()

