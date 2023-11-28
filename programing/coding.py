"""Module providing ui for python."""
'''
abandoned code
try:#check if tkinter installed or not
    import tkinter as tk#pip install tk or pip3 install tk
except ImportError:
    print("tkinter not installed")
"""Module  data saving funshion python."""
'''
try:
    import sys
except ImportError:
    print("sys is not installed")
try:
    import pygame #try to import pygame
except ImportError:
    print("pygame not imported") #report that pygame is not imported
try:
    import pickle #check if pickle installed or not
except ImportError:
    try:    
        import pickle5
    except ImportError:
        print("please install Pickle")
        print("type pip install pickle into terminal")  
#define funshion for data saving and loading using pickle
def data_save_load(method):
    if method==1:#loading
        try:
            with open("userdata", "rb") as namefile:   #try to load data
                namelist = pickle.load(namefile)#data loaded into list namelist
        except FileNotFoundError:
            print("data not found") #return fail
            with open('userdata', 'wb') as usr_file:
                usr_file.close()                
    if method==2:#saving
        try:
            with open("userdata", "wb") as namefile:#try to save data   #Pickling
                pickle.dump(namelist, namefile)            
        except FileNotFoundError:
            print("save failed") 
            print("data not found") #return fail
            with open('userdata', 'wb') as usr_file:#open a new file
                usr_file.close()                

''' 
abandoned code
def page(page_number):#set the page 1 
    global window
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    if page_number==1:
        window.title('page1-menu')
        window.geometry('500x300')
        choose1 = tk.Button(window, text='roll_call', command=page(2))
        choose1.pack()
    if page_number==2:
        window.title('page2-roll_call')
        window.geometry("%dx%d" % (width, height))
    window.mainloop()
'''

pygame.init()

def pygamestart():
    flags=pygame.FULLSCREEN
    screen.fill
    pygame.display.set_caption('scouting  system')
    pygame.display.flip()

def pygamepage(page_number):
    if page_number==1:  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

pygamestart()
pygamepage(1)
    