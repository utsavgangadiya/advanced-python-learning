num_list =[10,11,12,13,14,15,16,17,18,19]

def len_list (list):
    print( len(list))

len_list(num_list)

# 10

def list_item (list):
    for i in list:
        print(i,end=" ")

list_item(num_list)
print()
# 10 11 12 13 14 15 16 17 18 19 

# factorial

def cal_fact(num):
    fact = 1 
    for i in range (1,num+1):
        fact *= i
    return fact

print(cal_fact(5))

def con (usd):
    inr = usd *93
    print(usd , "USD = ",inr, "INR")

con(10)

# 

def odd_even(num):
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"
    
num = int(input("Enter num:"))
print(odd_even(num))
