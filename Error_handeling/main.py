a = input("enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} * {int(i)} = {int(a)*i}") #prone to error
except Exception as e:
    print(e)
    
print("some imp lines of code")
print("End of program")




#Specific type of errors:

try:
    b = int(input("Enter a number: "))
    arr = [1,2,3]
    print(arr[b])
    
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("the number entered resulted in index out of bound in the array")
    
