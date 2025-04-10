def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
     try:
         return x/y
     except:
         print("An exception occurred.")

def power(x,y):
    return x**y

def mod(x,y):
    return x%y

if __name__ == "__main__":
    print(add(4,2))
    print(subtract(4,2))
    print(multiply(4,2))
    print(divide(4,2))
    print(power(4,2))
    print(mod(4,2))
