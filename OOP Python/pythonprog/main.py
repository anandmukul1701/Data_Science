class Backpack:

    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.size = size


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.color = "Blue"


class Rectangle:

    def __init__(self, length, width):
        print("The value of self in Rectangle class is", self)
        print("Notice that value of self and the Object address is same")
        self.length = length
        self.width = width


class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_backpack = Backpack("Blue", "Small")

print(my_backpack)

my_circle = Circle(5)

print(my_circle)

my_rectangle = Rectangle(3, 6)

print(my_rectangle)


# Common Mistakes
# Omitting the def keyword:

# The def keyword is missing.
# __init__(self, width, height):
# 	self.width = width
# 	self.height = height


# Using only one underscore (You must use two):
# There should be two underscores before and after init.
# def _init_(self, width, height):
# 	self.width = width
# 	self.height = height


# Omitting self as the first parameter:

# Self is missing. It should be the first parameter.
# def __init__(width, height):
# 	self.width = width
# 	self.height = height


# Not using self.<attribute> to assign instance attributes:

# You should use self.<attribute> to assign them
# def __init__(self, width, height):
# 	width = width.
# 	height = height
