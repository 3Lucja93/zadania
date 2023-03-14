# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#        count += 1
#        print(number)
# print(f"We have {count} numbers")
#
# def greet1(first_name, last_name, age):
#     print(f"Hello {first_name} {last_name} {age}")
# greet1("uiedgeiu", "gxuyfc", "46")
#
# def greet(name) :
#     print(f"hi {name}")
# def get_greeting(name):
#     return f"hi {name}"
# print(greet("Lucja"))
#
# def multiply(*numbers):
#    # print(numbers)
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multiply(3, 4, 1))
#
# def save_user(**user):
#     print(user)
# save_user(id=1, name="John")

def FizzBuzz():
    tekst = ""
    for number in range(1, 100):
        if number % 15 == 0:
            tekst += "FizzBuzz\n"
        elif number % 3 == 0:
            tekst += "Fizz\n"
        elif number % 5 == 0:
            tekst += "Buzz\n"
        else:
            tekst += ""
    return tekst
print(FizzBuzz())


