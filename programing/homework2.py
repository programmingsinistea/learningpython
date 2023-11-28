import  math
//to tell user how the formula works
print("quadratic function: a*x**2 + b*x + c")
//make the list for teo answer
list=[]
//def the founction the can return the answer
def quadratic(d,e,f):
    temp=2*d   
    temp2=4*d*f
    temp3=e**2-temp2
    temp3=sql(temp3)
    ans1=abs(e)+temp3
    ans1=ans1/temp
    list.append(ans1)
    ans1=abs(e)-temp3
    ans1=ans2/temp
    list.append(ans)

a=int(input('a='))
b=int(input('b=))
c=int(input('c='))

quadratic(a,b,c)
print("there is two root"+list[0]+" and "+ list[1])
