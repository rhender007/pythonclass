'''
Created on Dec 1, 2016

@author: Student
'''
print("Creating a text file with the write() method.")
text_open = open("write_it.txt", "w")
text_open.write("Line 1\n")
text_open.write("This is Line 2\n")
text_open.write("This makes Line 3\n")
text_open.close()

print("Creating a text file with the writelines() method")
text_file = open("write_it.txt", "a")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()