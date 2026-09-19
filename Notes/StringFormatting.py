name = "John"
place = "New York"

#Syntax for string formatting -- Use for dynamic strings
print("Hello, my name is {}, I am from {}".format(name,place))

#Syntax for f-string formatting -- Latest and most preferred way of string formatting
print(f"Hello, my name is {name}, I am from {place}")

#Syntax for %-formatting
print("Hello, my name is %s, I am from %s" % (name, place))

# #Syntax for Template string formatting -- Not that useful
# from string import Template
# template = Template("Hello, my name is $name, I am from $place")
# print(template.substitute(name=name, place=place))

#Syntax for concatenation -- Use when creating string via some algorithm
print("Hello, my name is " + name + ", I am from " + place)

#Syntax for join method -- Use when creating string via some algorithm

a = ["Hello", "I", "am", "John"]
print("-/\-".join(a))

print("Hello, my name is " + " ".join([name]) + ", I am from " + " ".join([place]))

