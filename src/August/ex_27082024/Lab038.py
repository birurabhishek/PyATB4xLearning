def my_decorator(func):
    #Two parts
    #Wrap & call
    def wrapper():
        print("Something is happening before the function is called")
        print("Wear Helmet, Knee Guards, Dash cam")
        func() #drive_bike
        print("Something is happening after the function is called")
        print("Secure Driving")
    return wrapper()

@my_decorator
def drive_bike():
    print("I'm Driving")
