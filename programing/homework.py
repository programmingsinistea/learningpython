def quadratic(a,b,c)
    num=b**2
    num=num-4*a*c
    if num<0:
        numOfRoot=0
    elif num==0:
        numOfRoot=1
    elif num >0:
        numOfRoot=2   
    if numOfRoot >= 0:
        ans1=((-b)+num**0.5)/2*a
        ans2=((-b)-num**0.5)/2*a
        print("there is",str(numOfRoot),"root")
        ans1=str(ans1)
        print("x= "+ans1)
        if numOfRoot == 2:
            ans2=str(ans2)
            print("or x= "+ans2)
    else:
        print("there is not real root")
print("quadratic formula ax**2 + bx + c")
d=float(input("a= "))
e=float(input("b= "))
f=float(input("c= "))
quadratic(d,e,f)



