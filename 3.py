"""3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""


para="anagrams of a text are the word that text use the same letters as test given"
text=input("enter your letters: ")
para_list=para.split(" ")
for i in para_list:
    if text in i:
        print(i)
