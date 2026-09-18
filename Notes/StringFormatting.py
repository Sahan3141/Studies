#Syntax for string formatting
name = "John"
place = "New York"
print("Hello, my name is {0}, I am from {1}".format(name,place))

#Syntax for f-string formatting
name = "John"   
place = "New York"
print(f"Hello, my name is {name}, I am from {place}")

#Syntax for %-formatting
name = "John"
place = "New York"
print("Hello, my name is %s, I am from %s" % (name, place))

#Syntax for Template string formatting
from string import Template
name = "John"
place = "New York"
template = Template("Hello, my name is $name, I am from $place")
print(template.substitute(name=name, place=place))

#Syntax for concatenation
name = "John"   
place = "New York"
print("Hello, my name is " + name + ", I am from " + place)

#Syntax for join method
name = "John"   
place = "New York"
print("Hello, my name is " + " ".join([name]) + ", I am from " + " ".join([place]))