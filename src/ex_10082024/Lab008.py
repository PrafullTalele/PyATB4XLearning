# Variable is nothing but a container which stores a value.
age = 65
# (age) -> variable name or Container and (65) -> Value stored in (age) variable, Data type of the container -> integer.
print(age)
#age = variable name -> it is called as identifier.
# 123 = 34 -> Not possible - We can use A-Z or a-z.
a =10
print(a)

#3 Rules we have to follow for identifiers.
#1 They start with a letter (A-Z or a-z).
#2 An underscore (_) can be a variable name or An underscore
# followed by zero or more letters can be a variable name.
#3 Python is case-sensitive, So myVariable and myvariable are two different identifiers.

_ = 45
print(_)
_ = _+1
print(_)

abc123 = 78
#123abc = 90 -> it's not allowed
_pramod = "amit"
print(_pramod)
_abc = 23
print(_abc)
# $123 = 67 -> it's not allowed
# &123 = 23 -> it's not allowed

pi = 3.14 # Data type -> float
name = "Pramod" # Data type -> string (str)
isMale = True # Data type -> boolean (bool)
print(type(pi)) # we can check the data type by using a function called "type".
print(type(name))
print(type(isMale))

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)