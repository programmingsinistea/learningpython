from playsound import playsound
import time
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import time
import pickle

no =int(input("first time?type 1 if yes"))
if no == 1:	
    print("ans")
    data=[0,0,0]
    file = open('important', 'wb')
    pickle.dump(data, file)
    file.close()


else:
    print("ans")
    file = open('important', 'rb')
    data = pickle.load(file)
    file.close()
print("loaded")
 

image_list = ['popcat1.jpg', 'popcat2.jpg']
current = 0
pi=3.1415926
X=0
Y=0
X1=0
Y1=0
unknown=0
popcat = 0
name=0

if current == 2:
    time.sleep(0.5)
    image = Image.open(image_list[1])
def move(Rd):
    global current, image_list
    print("poplabel")
    if  current + Rd > len(image_list)  :
        current=0
    current += Rd
    print('current=',current)
    if current == 1 or current== 0 :
        image = Image.open(image_list[0])
    if current == 2:
        image = Image.open(image_list[1])
    photo = ImageTk.PhotoImage(image)
    label['image'] = photo
    label.photo = photo
def math1():
   global X
   global X1
   if X1 != 1:
       X = int(entry1.get())
   X=X**2
   X1=1
   button8["text"]="seted"  
def math2():
    global Y1
    global Y
    if Y1 !=1:
        Y1 = int(entry2.get())
    Y=Y**2
    Y1=1
    button9["text"]="seted"
def enterpi2():
    global Y
    global Y1
    Y=3.1415926  
    button7["text"]="seted"
    Y1=1
def enterpi():
    global X
    global X1
    X=3.1415926  
    button6["text"]="seted"
    X1=1   
def enter1(): 
    global unknown
    unknown=1
def enter2(): 
    global unknown
    unknown=2
def enter3(): 
    global unknown
    unknown=3
def enter4():
    global unknown
    unknown=4 
def no ():#def button
    global X
    global Y
    global X1
    global Y1
    ans=1
    if X1 != 1:
        X = int(entry1.get())
    if Y1 != 1:
        Y = int(entry2.get())
    button6["text"]="pi"
    button7["text"]="pi"   
    button["text"]="done"
    if unknown==1:
        ans = X+Y
    elif unknown==2:
        ans = X-Y
    elif unknown==3:
        ans = X*Y
    elif unknown==4:
        ans = X/Y
    text.delete("1.0",tkinter.END)
    text.insert("1.0",ans)
    X1=0
    button8["text"]="x²"
    button9["text"]="y²"
    Y1=0
def clickpopcat():
    global popcat
    global start_time
    popcat= popcat +1
    move(+1)
    playsound('"pop.mp3"')
    print(popcat)
    if popcat == 100:
        stop_time=time.time()
        used_time =stop_time - start_time

  
        print()
        if int(used_time) < data[0] or data[0] == 0:
            print("oooooooooooooooooooooooooooooooo")
            data[0]=used_time

        elif int(used_time) > data[0] and int(used_time) < data[2] or data[1] == 0:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            data[1]=used_time
        elif int(used_time) < data[2] or data[2] == 0:
            print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            with open('company_data.pkl', 'wb') as outp:
                 data[2]=used_time
        popcat=0
        start_time = time.time()
        file = open('important', 'wb')
        pickle.dump(data, file)
        file.close()
def refresh():
    print("--------------------------------------------------------------------------------------------------------------")

    button13["text"]= "1st  "+str(data[0])
    button14["text"]= "2nd  "+str(data[1])
    button15["text"]= "3rd  "+str(data[2])
    print("refreshed")




print('finished1')
print ("Hello World")
root=tkinter.Tk()
root.title("calculator")#title
root.geometry("750x750")
label = tkinter.Label(root, compound=tkinter.TOP)
label.pack()
label.place(x=220,y=300)
move(0)
button13 = tkinter.Button(text="1st  "+str(data[0]),command=refresh)
button13.place(x=350,y=150)
button14 = tkinter.Button(text= " 2nd  "+str(data[1]),command=refresh)
button14.place(x=350,y=200)
button15 = tkinter.Button(text="3rd  "+str(data[2]),command=refresh)
button15.place(x=350,y=250)
#win.geometry("700x300")


entry1 = tkinter.Entry(width=10)#entry2 set
entry2 = tkinter.Entry(width=10)#entry2 set
entry1.place(x=20, y=20)#entry1 place
entry2.place(x=200, y=20)#entry2 place
button= tkinter.Button(text="enter",command=no)#button set
button1= tkinter.Button(text="+",command=enter1)#button set
button2= tkinter.Button(text="-",command=enter2)#button set
button3= tkinter.Button(text="x",command=enter3)#button set
button4= tkinter.Button(text="÷",command=enter4)#button set
button6= tkinter.Button(text="pi",command=enterpi)#button set
button7= tkinter.Button(text="pi",command=enterpi2)#button set
button8= tkinter.Button(text="x²",command=math1)#button set
button9= tkinter.Button(text="y²",command=math2)#button set
button10= tkinter.Button(text="popcat",command=clickpopcat)#button set
button.place(x=300,y=20)#button place
button1.place(x=100,y=20)#button place
button2.place(x=120,y=20)#button place
button3.place(x=140,y=20)#button place
button4.place(x=160,y=20)#button place
button6.place(x=20,y=40)#button place
button7.place(x=200,y=40)#button place
button8.place(x=40,y=40)#button place
button9.place(x=220,y=40)#button place
button10.place(x=300,y=580)#button place
print('finished2')
text = tkinter.Text(width=20, height=1, font=("System",24))
text.place(x=370,y=17)
label2 = tkinter.Label(root, text="=",font=("System",24))
label2.place(x=350,y=17)

start_time = time.time()


print('activite')
root.mainloop()#activite
print('finished3')
