current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)



prompt = "Tell me something "
prompt += "(Enter 'quit' to end the program): "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


responses = {}

active = True
while active:
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("for end (yes/no): ")
    if repeat == "yes":
        print("quit...")
        active = False
        print(responses)

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")