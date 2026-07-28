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

# ex

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(10))

#ex

def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

print(calc_sum(10))

# ex

def list_item (list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])

    list_item(list,idx+1)

list = ["utsav","heli","sara"]
list_item(list)
