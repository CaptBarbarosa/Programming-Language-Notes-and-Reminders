file_stream = open("File_to_read.txt", "r")
print(file_stream.read())

print("With read(<number_of_characters>) you can read the specified amount of characters. For example: ")
file_stream = open("File_to_read.txt", "r")
print(file_stream.read(10))


print("Now reading line by line")

with open("File_to_read.txt", "r") as file_stream:
    for line in file_stream:
        print(line)


write_to_the_file = "Write this"
file_stream = open("Writer.txt", "w")
file_stream.write(write_to_the_file)
file_stream.close()
