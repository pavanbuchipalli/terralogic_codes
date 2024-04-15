


class shape:
    def area(self):
        pass


class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (0.5 * self.base * self.height)


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * self.radius * self.radius)



class mathematics():
    # while True:
        while True:
            selection = int(input("selct a shape of the object \n 1-circle \n 2-Triangle \n 3-Square \n choose a number from above :--"))
            if selection < 4 and selection > 0:
                print(f"You have selected : {selection}")

            else:
                print("Enter number only 1,2, and 3")
            if selection == 1:
                radius= int(input("selcet the radius value : ---"))
                c =Circle(radius)
                print("Radius of the circle",c.area())
                user_choice=input("You want to Termainate")
                if user_choice=="yes":
                    break

            elif selection ==2:
                data1 = int(input("select the base  value : ---"))
                data2 = int(input("select the height value : ---"))
                c = Triangle(data1,data2)
                print("Area of Traiangel ",c.area())
                user_choice = input("you want to termainate")
                if user_choice == "yes":
                    break

            elif selection == 3:
                data = int(input("select the side value : ---"))
                c = Square(data)
                print("Area of square is :--",c.area())
                user_choice = input("you want to termainate")
                if user_choice == "yes":
                    break


