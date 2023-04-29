https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python



# 1st soln 
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code her
    arr =[]
    for x in range(a,b+1):
        str_x = str(x)
        sum = 0 
        for index,item in enumerate(str_x):
            sum += (int(item) ** (index+1))
        if sum == x:
            arr.append(sum)
    return arr


# 2nd slution 
def check(x):
    return sum( int(b)**a for a,b in enumerate(str(x),1))
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    return [ x for x in range(a,b+1) if x == sum( int(b)**a for a,b in enumerate(str(x),1)) ]