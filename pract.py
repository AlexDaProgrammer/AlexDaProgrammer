"""
My answers to worksheet 2
"""

#libraries used total#
import math
from graphix import Circle, Point, Window, Rectangle
######################

#week 1 start####################################################################################################################################

def say_name():
    print("My name is Alex")

# say_name()



def say_hello2():
    print("hello")
    print("world")

# say_hello2()


def dollars_to_pounds():
    dollars = float(input("Enter amount in dollars:"))
    pounds = dollars * 0.87
    print("pounds:", pounds)

# dollars_to_pounds()


def sum_and_difference():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)

# sum_and_difference()


def change_counter():
    onep = int(input("Enter the number of 1p coins: "))
    twop = int(input("Enter the number of 2p coins: "))
    fivep = int(input("Enter the number of 5p coins: "))
    total = onep + twop * 2 + fivep * 5
    print("Total change in pence:", total)

# change_counter()


def ten_hellos():
    # i=0
    for i in range(10):
        print("hello")

# ten_hellos()


def zoom_zoom():
    i=int(input("Please enter a number: "))
    for z in range(i):
        print("zoom ",z+1)

# zoom_zoom()


def count_to():
    num = int(input("Enter a number: "))
    for i in range(1, num + 1):
        print(i)

# count_to()


def count_from_to():
    start=int(input("Enter the first number:"))
    end=int(input("Enter the second number:"))
    for i in range(start,end+1):
        print(i)

# count_from_to()


def weights_table():
    print("KG:\tOUNCES:")
    for i in range(10,101,10):
        print(f"{i}:\t {i * 35.274}")

# weights_table()


def future_value():
    initial_amount = float(input("Enter the initial amount: "))
    years = int(input("Enter the number of years: "))
    for i in range (years):
        # initial_amount += initial_amount * 0.035
        initial_amount = initial_amount * 1.035

    print("Final value of investment:", initial_amount)

# future_value()

#week 1 end####################################################################################################################################

#week 2 start####################################################################################################################################
def pytheorem():
    x1=3
    x2=5
    y1=4
    y2=7
    dx=x2-x1
    dy=y2-y1
    #d^2=(dx^2)+(dy^2)

    d=math.sqrt( (dx**2)+(dy**2) )
    print(d)
#ex1
def speed_calculator():
    dt = int(input("Please provide the distance traveled: "))
    dur = int(input("Please provide the duration of the journey in hours: "))
    print (float(dt)/dur)
#ex2
def circumference_of_circle():
    radius=float(input("Please provide the radius of the circle: "))
    print(round(2*math.pi*radius, 2))
#ex3
def area_of_circle():
    radius=float(input("Please provide the radius of the circle: "))
    print(round(math.pi*radius**2,2))
#ex4
def cost_of_pizza():
    diameter=float(input("Please provide the diameter of the pizza: "))
    print(round((math.pi*((diameter/2)**2))*3.5/100),2)
#ex5
def slope_of_line():
    x_1 = float(input("Enter x1: "))
    y_1 = float(input("Enter y1: "))
    x_2 = float(input("Enter x2: "))
    y_2 = float(input("Enter y2: "))
    print("Slope: " , (y_2 - y_1) / (x_2 - x_1))
#ex6 
def distance_between_points():
    x_1 = float(input("Enter x1: "))
    y_1 = float(input("Enter y1: "))
    x_2 = float(input("Enter x2: "))
    y_2 = float(input("Enter y2: "))
    print(math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2))
    #print(math.hypot(x_2 - x_1, y_2 - y_1))
#ex7
def travel_statistics():
    speed = float(input("Please provide the average speed: "))
    dur = float(input("Please provide the duration: "))
    print("Distance",speed*dur,"km")
    print("Fuel Consumption: ",speed*dur/5,"litres")
#ex8
def sum_of_squares():
    """
    a function that returns the sum of squares of numbers
    """
    n=int(input())
    total=0
    for i in range (1,n+1):
        total += i**2
    print("Sum is: ",total)

# sum_of_squares()

#ex9
def average_of_numbers():
    n=int(input("How many numbers to input? "))
    total = 0
    for _ in range(n):
        total+=int(input())
    print(float(total)/n)
#ex10
def fibonacci():
    current=1
    prev=0
    n=int(input("Give the number: "))
    for i in range (n):
        temp=current
        current+=prev
        prev=temp
    print(prev)
#ex11
def select_coins():
    p = int(input("Provide the amount of pence: "))
    print(p // 200, "x £2")
    p %= 200
    print(p // 100, "x £1")
    p %= 100
    print(p // 50, "x 50p")
    p %= 50
    print(p // 20, "x 20p")
    p %= 20
    print(p // 10, "x 10p")
    p %= 10
    print(p // 5, "x 5p")
    p %= 5
    print(p // 2, "x 2p")
    p %= 2
    print(p, "x 1p")
#week2 end####################################################################################
#week3 start##################################################################################
#Solutions
#Use these after attempting and discussing each example.
#Example 1 solution
#Create a window and a point, then inspect the point coordinates.
#from graphix import Window, Point
win = Window("First window", 400, 400)
point = Point(30, 90)
print(point.x, point.y)


#Example 2 solution
#Create, colour and draw a circle. Wait for a click before closing.
from graphix import Window, Point, Circle
win = Window("Circle", 400, 400)
circle = Circle(Point(200, 200), 50)
circle.fill_colour = "red"
circle.draw(win)
win.get_mouse()
win.close()


#Example 3 solution
#Move the circle after a click.
from graphix import Window, Point, Circle
win = Window("Move", 400, 400)
circle = Circle(Point(100, 200), 30)
circle.draw(win)
win.get_mouse()
circle.move(100, 0)
win.get_mouse()
win.close()


#Example 4 solution
#Draw a small blue circle wherever the user clicks.
from graphix import Window, Point, Circle
win = Window("Click", 400, 400)
click = win.get_mouse()
marker = Circle(Point(click.x, click.y), 8)
marker.fill_colour = "blue"
marker.draw(win)
win.get_mouse()
win.close()


#Example 5 solution
#Improve the names and extract the drawing into a function.
def draw_marker(window, x, y):
    marker = Circle(Point(x, y), 10)
    marker.fill_colour = "blue"
    marker.draw(window)


#Example 6 solution
#Choose three useful click positions for the marker program and state what each tests.
#Centre: Point(200, 200)
#Near top-left: Point(5, 5)
#Near bottom-right: Point(395, 395)

def simple_point():
    width=int(input("Give me the width of the window: "))
    height=int(input("Give me the height of thr window"))
    win = Window("",width,height)

    win.get_mouse()
    win.close()

def simple_rectangle():
    win= Window("",500,500)
    p1= win.get_mouse()
    p2=win.get_mouse()
    rect = Rectangle(p1, p2)
    rect.fill_colour = "blue"
    rect.draw(win)

    win.get_mouse()
    win.close()

def simple_circle():
    win= Window("",500,500)
    center= win.get_mouse()
    radius= 30
    circle= Circle(center, radius)
    cicle.fill_colour = "red"
    circle.draw(win)
    win.get_mouse()
    win.close()
