# Camel Case:
myVariableName = "Jason"
print(myVariableName)

#Pascal Case:
MyVariableName = "Ferb"
print(MyVariableName)

#Snake Case:
my_variable_name = "Anne"
print(my_variable_name)

# Assign Multiple values.

#Many values to multiple variable
x,y,z="orange","mango","apple"
print(x)
print(y)
print(z)

# One value to multiple Variable
x=y=z="Banana"
print(x)
print(y)
print(z)

# Unpack a collection
fruits =["apple","cherry","Mangoes"]
x,y,z = fruits
print(x)
print(y)
print(z)

# Output Variable
x="awesome"
print("Python is "+ x)

x="Python is "
y="awesome"
z=x+y
print(z)

x = 5
y = 8
print(x+y)
''' you cannot combine string and integer together.
x = 5
y = "jason"
print(x+y)
'''

# Global Variable
x="awesome"

def myfunc():
    print("Python is "+ x)
    
    
myfunc()

# Example 2
x = "awesome"

def myfunc():
    x = "Fanatastic"
    print("Python is "+ x)
    
myfunc()
print("Python is "+ x)

# Global Keyword:
def myfunc():
    global x
    x="fanatastic"
    
myfunc()
print("Python is "+x)