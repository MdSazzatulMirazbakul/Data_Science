# print("Hello My Friends")
# print(2+2)
# Name = "Bakul"
# age = 29
# print(f"My name is {Name}, and my age is {age}")


""" Lambda with builtin functions"""
from pygments.lexer import words

" Using Lambda function with map function"

# Numbers = [4, 5, 6, 7, 8, 9, 10]
# doubled = list(map(lambda x: x * 2, Numbers))
# print(doubled)

# Numbers = [1, 2, 12, 15, 17, 23, 28, 32, 35, 36]
# Odd_numbers = list(filter(lambda x : x % 2 ==0, Numbers))
# print(Odd_numbers)

""" For Loop"""
sales = [200, 300, 350, 200, 500, 430, 150]
total = 0
for s in sales:
    total = total + s
print("Total sale: ", total)

"""range"""
for i in range(1, 6):
    print("inv_2026", i)

""""While Loop"""
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# stock = 10
# while stock > 0:
#     print("Item Sold")
#     stock -= 1

stock = 5
while stock > 1:
    print("Eaten Choclet")
    stock -= 1

"""Break or stop loop"""
# for item in range(10):
#     if item == 5:
#         break
#     print(item)

# list = [10, 5, -1, 3, 6]
# for item in list:
#     if item < 0:
#         continue
#     print(item)

"""Nested Loop"""

# for i in range(5):
#     for j in range(6):
#         print(i, j)

# stores = ["store A", "store B"]
# days = ["Monday", "Tuesday"]
# for store in stores:
#     for day in days:
#         print(store, day)

"""Condition and Logics"""
# Sales = [200, 150, 230, 400, 350, 430, 500]
# for sale in Sales:
#     if sale >200:
#         print("High Sale: ", sale)

"""" Loop with enumeration"""

# sale = [200, 300, 350, 400, 500]
# for index, value in enumerate(sale):
#     print(index, value)

"""Loop with zip"""
# products = ["A", "B", "C"]
# prices = [10, 15, 20]
# for product, price in zip(products, prices):
#     print(product, price)

"""List Comprehension"""
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [n*n for n in numbers]
# print(squared)

sales = [150, 200, 230, 300, 400, 500]
high_sales = [s for s in sales if s >= 200]
print(high_sales)

# Numbers = [3, 5, 4, 7, 8, 5]
# square = [s*s for s in Numbers]
# print(square)

Sales_data = [200, 150, 300, 400, 100, 350, 450]

total = 0
high_sale = 0
for s in Sales_data:
    total += s

    if s > 300:
        high_sale += 1

        print("Total: ", total)
        print("High Sale: ", high_sale)

# marks = [40, 80, 90, 30, 70]
# total = 0
# high_marks = 0
# for m in marks:
#     total += m
#
#     if m > 50:
#         high_marks += 1
#
#         print("Total Marks: ", total)
#         print("How many marks > 50: ", high_marks)
#
import pandas as pd
# data = {
#     "Day": ["Mon", "Tue", "Wed", "Thus", "Fri"],
#     "Sale": [220, 300, 350, 250, 320]
# }

# df = pd.DataFrame(data)
# print(df)
#
# for s in df["Sale"]:
#     print(s)
#
# for index, row in df.iterrows():
#     print(row["Day"], row["Sale"])

# for index, row in df.iterrows():
#     if row["Sale"] > 250:
#         print(row["Day"], "High Sale")


# import pandas as pd
# pf = pd.read_excel("sales_data.xlsx")
# print(pf)

def greet_user(name):
    print("Hello, ", name)

greet_user("Bakul")

def login(username):
    print(f"Welcome {username}!")

login("Md Sazzatul Miraz Bakul")

def signup(username, password):
    print(f"{username} {password}")

signup("MdSazzatul", 1223)


def square(number):
    return number * number
result = square(12)
print(result)

def celcius_to_farenheit(c):
    return (c * 9/5) + 32
print(celcius_to_farenheit(39))

def full_name(first, last):
    return first + " " + last
print(full_name("Md Sazzatul Miraz", "Bakul"))

def total_size(file1, file2):
    return file1 + file2
print(total_size(200, 300))

def power(base, exponent= 2):
    return base ** exponent
print(power(5))
print(power(5, 3))

def resize(width, height=100):
    return f"image resized to {width}*{height}"
print(resize(200))
print(resize(100, 200))

""""Keyword Argument"""
def create_profile(Name, Age, City):
    print(Name, Age, City)

create_profile(Name = "Bakul", Age= 28, City= "pesaro")

def analyze_text(text):
    length = len(text)
    words = len(text.split())
    return length, words
l, w = analyze_text("Python is fun")
print()

print("length: ", l)
print("words: ", w)

def number_info(n):
    return n, n*n, n*n*n
num, square, cube = number_info(5)
print(num)
print(square)
print(cube)