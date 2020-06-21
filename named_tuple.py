from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,5)
dot_prod = (pt1.x*pt2.x)+(pt1.y+pt2.y)
print(dot_prod)

# using namedtuple datastructures in python, we can easily call every instance of the tuple as predefined form.
# We can think of this like vectorized form

Car = namedtuple('Car','Price Mileage Color Class')
benz = Car(Price = 100000, Mileage = 20, Color = 'Black', Class = 'C')
bmw = Car(Price = 1000000, Mileage = 17, Color = 'Grey', Class = 'M')
kodia = Car(9090909, 8, 'Blue','F')
print(benz)
print(Car)
print(kodia)
