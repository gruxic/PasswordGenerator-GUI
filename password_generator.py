from tkinter import *
import random
import string
import pyperclip as pc

#Basic Outline          
root= Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Password Generator - By gru")
Label(root, text="Password Generator", font='arial 15 bold').grid()
Label(root, text="By gruxic", font='arial 8 bold').grid(row=10,column=0)



sym_key= BooleanVar()
Checkbutton(root, text="Include Symbols", variable=sym_key ).grid(row=1,column=3)
dig_key=BooleanVar()
Checkbutton(root, text="Include Digits", variable=dig_key ).grid(row=2,column=3)
upper_key= BooleanVar()
Checkbutton(root, text="Include Uppercase", variable=upper_key ).grid(row=3,column=3)


pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').grid(row=1,column=0)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).grid(row=2,column=0)
pass_str = StringVar()

Button(root, text = "GENERATE PASSWORD" , command = lambda: pass_str.set(passcode(pass_len.get(),dig_key.get(),upper_key.get(),sym_key.get())) ).grid()
Entry(root , textvariable = pass_str, width=40).grid()
Button(root, text="COPY TO CLIPBOARD", command= lambda: pc.copy(pass_str.get())).grid(row=6,column=0)

def passcode(size,d,u,s):
    digits= list(string.digits)
    lower_case= list(string.ascii_lowercase)
    upper_case= list(string.ascii_uppercase)
    symbols= list(string.punctuation)
    comb8 = lower_case
    comb2 = digits+lower_case+upper_case
    comb3 = digits+lower_case+symbols
    comb4 = digits+lower_case
    comb5 = lower_case+upper_case+symbols
    comb6 = lower_case+upper_case
    comb7 = lower_case+symbols
    comb1 = digits+lower_case+upper_case+symbols
    

    r_digit=random.choice(digits)
    r_lcase= random.choice(lower_case)
    r_ucase= random.choice(upper_case)
    r_symb= random.choice(symbols)

    # CASE 1
    if(d==True & u==True & s==True):
        temp_pass=r_digit+r_lcase+r_symb+r_ucase
        for n in range(size-4):
            temp_pass=temp_pass+ random.choice(comb1)
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password

    # CASE 2
    elif((d is True)  and (u is True) and (s is False)):
        temp_pass=str(r_digit)+str(r_lcase)+str(r_ucase)
        for n in range(size-3):
            temp_pass=temp_pass+ str(random.choice(comb2))
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password

    # CASE 3
    elif((d==True) & (u==False) & (s==True)):
        temp_pass=r_digit+r_lcase+r_symb
        for n in range(size-3):
            temp_pass=temp_pass+ random.choice(comb3)
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password

    # CASE 4
    elif((d==True)  & (u==False) & (s==False)):
        temp_pass=str(r_digit)+r_lcase
        for n in range(size-2):
            temp_pass=temp_pass+ str(random.choice(comb4))
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password   

         # CASE 5
    #CASE 5
    elif((d==False)  & (u==True) & (s==True)):
        temp_pass=r_lcase+r_symb+r_ucase
        for n in range(size-3):
            temp_pass=temp_pass+ random.choice(comb5)
        temp_pass_l=list(temp_pass)

        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password


    # CASE 6
    elif((d==False)  & (u==True) & (s==False)):
        temp_pass=r_lcase+r_ucase
        for n in range(size-2):
            temp_pass=temp_pass+ random.choice(comb6)
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password

    # CASE 7
    elif((d==False) & (u==False) & (s==True)):
        temp_pass=r_lcase+r_symb
        for n in range(size-2):
            temp_pass=temp_pass+ random.choice(comb7)
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password

    # CASE 8
    elif((d==False) & (u==False) & (s==False)):

        temp_pass=r_lcase
        for n in range(size-1):
            temp_pass=temp_pass+ str(random.choice(comb8))
        temp_pass_l=list(temp_pass)
        
        password= sorted(temp_pass_l, key=lambda k: random.random())
        f_password=''
        for char in password:
            f_password=f_password+char
        return f_password



root.mainloop()  
