def great_user(user):
    #
    print(f"hello, {user}")

great_user('ap')


def student(name, age):
    print(name)
    print(age)

student("Ali", 20)

"""
def hi():
    print(input("tell me:"))
hi()
"""

fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    print(i, fruits[i])


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def add(a, b):
    c = a + b
    print(c)

result = add(2, 3)


def add(a, b):
    return a + b

result = add(2, 3)
print(result)


def calc(a, b):
    return a + b, a * b

s, m = calc(2, 3)

print(s)
print(m)
print("-" * 30)


def num():
    current_number = 0

    while current_number < 10:
        current_number += 1

        if current_number % 2 == 0:
            continue

        print(current_number)
num()


def pro():
    prompt = "Tell me something "
    prompt += "(Enter 'quit' to end the program): "
    message = ""
    while message != 'quit':
        message = input(prompt)
        print(message)
pro()

