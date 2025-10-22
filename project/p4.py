name = input("What is your name? ")
age = int(input("What's your pet's age? "))
pet_type = input("What type of animal is your pet? ")

print("Hi! Your name is", name)

if pet_type == "cat":
    human_age = age * 8
    print("Your cat's age in human years is", human_age)
elif pet_type == "dog":
    human_age = age * 7
    print("Your dog's age in human years is", human_age)
else:
    print("Pet type not recognized.")
