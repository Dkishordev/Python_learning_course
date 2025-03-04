


#string indexing
spam = 'Hello, world!'
print(spam[0]) #prints H
print(spam[4]) #prints o
print(spam[-1]) #prints !
print(spam[0:5]) #prints Hello
print(spam[:5])  #prints Hello
print(spam[7:]) #prints world!

#string operations
spam ="Hello world!"

print(spam.upper())
print(spam.lower())
print(spam.replace("world","Bob"))
print(spam.split())
text=['My', 'name', 'is', 'Bob']
print(' '.join(text))

spam=" Hello World! "
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

"""
validate user input exercise
username is no more than 12 characters
username must not contin spaces
username must not contain digits
"""

username=input("Enter a username: ")

if len(username)> 12:
    print("Username contains more than 12 characters.")
elif not username.find(" ") == -1:
    print("Username must not contin spaces.")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print(f"Hello {username}!")