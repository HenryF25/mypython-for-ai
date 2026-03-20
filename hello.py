user_name = input("please enter your name: ")
user_age = int(input("please enter your age: "))
user_height = float(input("please enter your height: "))
user_weight = float(input("please enter your weight: "))
print(
    f"your name is {user_name} you are {user_age} years old, you are {user_height} in height and {user_weight} in weight"
)

if user_age >= 18:
    print("you are of age")
else:
    print("you are underage")

if user_height < 5:
    print("you are short")
else:
    print("you are tall")

if user_weight < 30:
    print("you need more nutrient and you can't register")
else:
    print("you are healthy, you can register")
    print(input("tell me more about youself: "))
print(
    input(
        "good to hear about you but i will like to test your reasoning. should i proceed answer yes or no: "
    )
)
print(int(input("5 + 5: ")))
print(int(input("10 * 2: ")))
input("Email for registeration: ")
print("Thanks for registering you are now a member ")

user1 = {
    "User Name": user_name,
    "User Age": user_age,
    "User Height": user_height,
    "User Weight": user_weight,
}
print("welcome", user_name)
for keys, values in user1.items():
    print(f" * {keys}: {values}")
