with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", 'w') as file:
    file.write("Hello, my name is Daniel.")

with open("my_file.txt", 'a') as file:
    file.write("New text.")
