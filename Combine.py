def areacircle (x):
    return x * x *3.1416
def circumference (x):
    return x * 2 * 3.1416
def arearectangle (x, y):
    return x * y
def perimeterrectangle (x, y):
    return x + x + y + y
def areasquare (x):
    return x * x
def perimetersquare (x):
    return x * 4
def volumecube (x):
    return x * x * x
def volumerectangle (x, y, z):
    return x * y * z
def volumesphere (x):
    return 1.3 * 3.1416 * (x * x * x)
Whassup = True
while Whassup == True:
    print("Welcome, this can help you determine the area, perimeter, and volume of a shape")
    print("Choose an operator\n1.Square")
    print("2.Rectangle\n3.Circle")
    print("4.Exit")
    operator=(input("Enter operator: "))
    unit=(input("Enter Unit: "))
    if operator == '4':
        Whassup = False
        break
    #square
    elif operator == '1':
        print("1.Area\n2.Perimeter")
        print("3. Volume")
        operatorsquare = input("Enter 1 for area, 2 for perimeter, 3 for volume: ")
        length = float (input("Enter length: "))
        if operatorsquare == '1':
           print("The area is ", areasquare(length), "sq", (unit))
        elif operatorsquare =='2':
           print("The perimeter is ", perimetersquare(length))
        elif operatorsquare == '3':
            print("The volume is ", volumecube(length),"cubic", (unit))
    #Rectangle
    elif operator == '2':
        print("1.Area\n2.Perimeter")
        print("3.Volume")
        operatorrectangle = input("Enter 1 for area, 2 for perimeter, and 3 for volume: ")
        length = float (input("Enter length: "))
        width = float (input("Enter width: ")) 
        height = float (input("Enter height"))
        if operatorrectangle == '1':
            print("The area is ", arearectangle(length, width))
        elif operatorrectangle =='2':
            print("The perimeter is ", perimeterrectangle(length, width), "sq", (unit))
        elif operatorrectangle =='3':
            print("The volume is ", volumerectangle(length, width, height), "cubic", (unit))
    #Circle
    elif operator == '3':
        print("1.Area\n2.Circumference")
        operatorcircle = input("Enter 1 or 2 to enter an operation(only one digit): ")
        radius = float (input ("Enter radius: "))
        if operatorcircle == '1':
            print("The area of the circle is", areacircle(radius))
        elif operatorcircle == '2':
            print("The circumference of the circle is", circumference(radius), (unit))
        elif operatorcircle == '3':
            print("The volume of the sphere is", volumesphere(radius), "cubic", (unit))