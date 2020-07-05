"""11. Create a variable, filename. Assuming that it has a three-letter extension,
 and using slice operations, find the extension. For README.txt, the extension should be txt.
Write code using slice operations that will give the name without the extension.
Does your code work on filenames of arbitrary length?"""
filename=input("enter your file name: ")
[name,ext]=filename[:-3],filename[-3:]
if(ext=="txt"):
    print("it is a text file.")
else:
    print("it's not a text file.")
print(f"the file name is: {name}")