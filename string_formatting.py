#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
#print(data)
format_string = "Hello"

name= data[0] +" "+ data[1]

print(" %s %s. Your Current balance is $%d" %(format_string ,name, data[2]))
