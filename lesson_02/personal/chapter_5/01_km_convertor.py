#Write a program that asks the user to enter a distance in kilometers, and then converts that
#distance to miles. The conversion formula is as follows:
#Miles = Kilometers * 0.6214

def miles():
    kilometers = float(input("enter kilometers :"))
    miles = kilometers * 0.6214
    print("distance travelled in miles :{0:2f}".format(miles))
miles()
