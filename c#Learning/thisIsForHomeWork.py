k = int(input("k= "))
def summation(o):
    '''function calculate summation'''
    string=""
    temp = int()
    for i in range(1,o+1):
        temp = temp * (o*i)
        string = string + str(temp)
    return string
print(summation(k)) 
