# FileNotFound
# with open("file.txt") as file:
#     file.read()

try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["foo"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
# Will be triggered, if try succeeds
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

