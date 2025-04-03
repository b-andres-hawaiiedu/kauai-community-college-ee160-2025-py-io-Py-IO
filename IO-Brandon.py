# Write a script that prompts the user for input. Store that input in a variable, and print it back to the screen.

input1 = input("Please enter something to put to the screen: ")
print(f"\nYou wrote: {input1}")

# Open a text file and store the user's input. Remember to close the file!

input2 = input("\nPlease enter something to write to a file: ")

# Opens the file to be written
file2 = open("IO-text.txt", "w")
file2.write(input2)
file2.close()

# Opens the same file to be read
file2 = open("IO-text.txt", "r")
print(f"\nNow the file says: {file2.read()}")
file2.close()

# Ask the user for another input. Re-open the file, but this time APPEND the text to the file.

input3 = input("\nNow enter something to append to that file: ")

# Opens the file to be written
file3 = open("IO-text.txt", "a")
file3.write(input3)
file3.close()

# Opens the same file to be read
file3 = open("IO-text.txt", "r")
print(f"\nNow the file finally reads: {file3.read()}")
file3.close()