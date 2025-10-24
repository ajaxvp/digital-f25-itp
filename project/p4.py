name = input("What is your name? ")
pet_age_text = input("What's your pet's age?")
pet_age = int(pet_age_text)
pet_type = input("What type of animal is your pet? ")

print("Hi! Your name is", name)

if pet_type == "cat":
    human_age = pet_age * 8
    print("Your cat's age in human years is", human_age)
if pet_type == "dog":
    human_age = pet_age * 7
    print("Your dog's age in human years is", human_age)
