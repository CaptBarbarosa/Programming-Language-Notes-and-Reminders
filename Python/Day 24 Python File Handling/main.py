""" 
I used the following youtube video too:
1.) https://www.youtube.com/watch?v=Uh2ebFW8OYM

"""


with open("file.txt", "r") as f:
    print(f.name)
    f_contents = f.readlines() #If you said readline it just reads 1 line.
    print(f_contents)
    f.close()
    

with open("file.txt", "r") as f:
    for line in f:
        print(line, end='')
    f.close()

# In read() you can specify the number of characters to read in read(). Example read(100) will read first 100 characters.

with open("file.txt", "r") as f:
    contents = f.read(50)
    print(contents)

with open("my_file.txt", "w") as file: # This creates my_file.txt if it doesn't exist.
    file.write("\nNew text.")


