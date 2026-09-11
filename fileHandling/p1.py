#WRITING A FILE IN PYTHON


#OPENING A FILE IN PYTHON

f = open("example.txt", "w")  # Open the file in write mode
f.write("Hello, World!\n")  # Write a line to the file
f.close()  # Close the file
f = open("example.txt", "r")  # Open the file in read mode
hi = f.read()  # Read the content from the file
print(hi)  # Print the content read from the file
f.close()  # Close the file