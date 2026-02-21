# def greet():
#     print("Hello world")
#
# greet()
#
# def greet_person(name):
#     print("Hello", name)
#
# greet_person("Uvejsi")
#
# def greet2(name):
#     global message
#
#     message = f"Hello, {name}"
#     print(message)
#
# greet2("Blina")
# print(message)
#
# greeting = "Hello"
# name = "Uvejs"
#
# def greet():
#     global greeting
#     greeting = "goodbye"
#
#     name = "Dren"
#     message = f"{greeting}, {name} "
#     print(message)
#
# greet()



def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name} "
    return message

metoda1 = greet_person("MIlot1")

metoda2 = greet_person("Donart", "Hi")

print(metoda1)
print(metoda2)