#simple calculator

#calculation functions
def add(x, y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y





 #take user input
print("First number:")
userdef1 = int(input())
print("Function:")
func = input()
print("Second number:")
userdef2 = int(input())

#Main loop
while True:
    #determine and return function
    if func == "+":
        res = add(userdef1, userdef2)
        break
    elif func == "-":
        res = sub(userdef1, userdef2)
        break
    elif func == "*" or "x" or "X":
        res = mul(userdef1, userdef2)
        break
    elif func == "/":
        res = div(userdef1, userdef2)
        break
    else:
        print("error")
print("Result: " + str(res))