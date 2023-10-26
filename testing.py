#This code was wrote when I was a noob who knew nothing about sorting.
#so it is very very ugly and disgusting
#pls dont read
import random
import matplotlib.pyplot as plt
import numpy as np

stort_value = 0#Damn it so many Variation
string=0
box=0
max_num=0
storted=False
tryed=0
trylist=[]
sortlist=[]
i=0
list =[]
#show that the number in list for first to last number
def list_show():
    print("-------------------------------------------------------------------------------------------------------------")
    global string
    for i in list:
        print("list=",i)
        string=string + i
    print(list[0])
    print("sum=",string)  
def list_gen():
    global string  
    global max_num #oh my god how come it had so many global
    global i
    max_num = int(input("how many number you want to gen?"))
    while i < max_num:
        number = random.randint(1,max_num)
        print(number)
        list.append(number)
        i+=1    
# generate the list to sort
list_gen()
# the list before sorting
list_show()
p=input("press enter to start sorting")
def switch_number(d):
    x=d-1
    y=list[d]
    list[d]=list[x]
    list[x]=y
def list_testing():
    global sorted
    sorted= False
    for c in range(0,len(list)):    
        global box
        no = 0
        if list[c]>box:
            sorted=False 
        else:
            print("no.",c,"is sorted")
            no+=1
        box=list[c]
        if sorted!=True:
            break
def findmax():
    d=0
    max0=0
    min0=list[1]
    for i in list:
        if i > max0:
            max0=i
            print ("max=",max0)
            for i in list:
def list_sorting():
    box1=list[0]
    global stort_value#just disgusting ewwwwww
    global sorted
    global tryed
    global sortlist
    global trylist
    stort_value = 0
    tryed+=1
    #trylist.append(int(trylist))
    d=0
    for d in range(stort_value,len(list)):
        stort_value+=1
        if list[d] > box1:
            switch_number(d)
            sorted = False
            sortlist.append(int(stort_value))
            break
        if stort_value==len(list)-1:
            sorted = True
            break
        box1=list[d]
        d+=1
chose=int(input("1 for sorting 2 for max finding")) 
if chose==1:
    while True:
        list_sorting()
        print("sorting,tried",tryed)
        print("sorted",stort_value)     
     #loading_screen() #not finish yet
        if sorted == True:
            list_show()
            break
if chose==2:
    findmax()
    #to conclude
#readbility:0
#elegant:0
#efficiency:0

    
