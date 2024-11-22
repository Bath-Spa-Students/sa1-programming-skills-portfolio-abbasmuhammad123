#FUNCTIONS

# Void function 
def print_message():
    print("Abbas")
# Calling function 
print_message()

# Local variable 
def print_message():
    message ="Canada"  # Local variable 
    print(message)
# Calling function 
print_message()
# If i call this message it shows an error 

def print_message():
    m ="hello world"  # Local variable 
    print(m)
    print(m)     # message is not defined bcz local varaible is inside of program 

print_message()


#Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message ="abbas"
  print(message)
  
def print_message_2():
  message ="the best coder"
  print(message)

print_message()
print_message_2()

# Paasing argument to variable   

def print_message_2(world):  # parameter 
  print(world)

text ="hi welcome to bathspa university"
print_message_2(text)  # Argument 

#Example  parameter x store value and get double 
def main():
    value_num =50
    show_double(value_num)
    
def show_double(y):
      print(y*2)

main()

# Passing Multiple arguments 