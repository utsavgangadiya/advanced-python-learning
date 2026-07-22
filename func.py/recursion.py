def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
show(10)


# ex

def odd_even(num):
    if num < 0:
        num = -num   # Handle negative numbers

    if num == 0:
        return "even"
    if num == 1:
        return "odd"

    return odd_even(num - 2)


print(odd_even(9))   
print(odd_even(10))  
print(odd_even(-15)) 
print(odd_even(21))  

# 
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(10))
