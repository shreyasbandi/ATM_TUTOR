from tkinter import*
import tkinter.messagebox as tsmg
a_root=Tk()
a_root.geometry('1500x1000')
Label(text='Welcome To ME Bank',bg='orange',fg='white',font=('roman 45 bold'),padx=10,pady=8).pack(fill='x')
a=Frame(a_root,bg='skyblue',borderwidth=15,relief='sunken')
a.pack(side='left',fill='y')
def password():
    b=Frame(a_root,bg='light green',borderwidth=10,relief='sunken')
    b.pack(side='right',fill='y')
    password1=StringVar()
    atmnumber=StringVar()
    Label(b,text='your password should contain atleast 8 characters\ncontain atleast one special character\n NOTE\nAtm number is greater than 5',font=('roman 15 '),pady=5,padx=5,bg='light green').grid(row=0,column=0)
    Label(b,text='create password',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=1,column=0)
    Label(b,text='ATM number',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=2,column=0)
    aaa=Entry(b,textvariable=password1)
    aaa.grid(row=1,column=1)
    aab=Entry(b,textvariable=atmnumber)
    aab.grid(row=2,column=1)
    def dum():
        aq=f"{aaa.get()}"
        bw=f"{aab.get()}"
        if len(aq)>8 and len(bw)>5 and aq.isalnum()==False:
            
            a=[1000,12000,13456,1144,20000]
            import random
            s=random.choice(a)
            k=open(bw+aq,'w')
            k.write(str(s))
            k.close
            
            tsmg.showinfo('Me Bank',f"your account has been created and your amount in account is {s}")
            b.destroy()
        else:
            tsmg.showinfo('Me Bank','your password is not meating requirements')
    Button(b,text='Create Account',command=dum).grid(row=3,column=1)

def withdraw():
    c=Frame(a_root,bg='light green',borderwidth=10,relief='sunken')
    c.pack(side='right',fill='y')
    password1=StringVar()
    atmnumber=StringVar()
    amount1=StringVar()
    Label(c,text='Enter password',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=0,column=0)
    Label(c,text='ATM number',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=1,column=0)
    Label(c,text='Enter amount',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=2,column=0)
    aaa=Entry(c,textvariable=password1)
    aaa.grid(row=0,column=1)
    aab=Entry(c,textvariable=atmnumber)
    aab.grid(row=1,column=1)
    aac=Entry(c,textvariable=amount1)
    aac.grid(row=2,column=1)
    
    

    def raw():
        aq=f"{aaa.get()}"
        b=f"{aab.get()}"
        amf=f"{aac.get()}"
        e=int(amf)
        a=open(b+aq,'r')
        cz=a.read()
        d=int(cz)
        if d>=e:
            z=d-e
            cv=str(z)
            x=open(b+aq,'w')
            x.write(cv)
            x.close()
            tsmg.showinfo("Me Bank",f"Amount in your account after this transaction is {cv}")
            c.destroy()
        else:
            tsmg.showinfo("Me Bank",f"Amount in your account is less to make this transaction")

    Button(c,text='submit',command=raw).grid(row=3,column=1)

    
    

def deposit():
    b=Frame(a_root,bg='light green',borderwidth=10,relief='sunken')
    b.pack(side='right',fill='y')
    password1=StringVar()
    atmnumber=StringVar()
    amount1=StringVar()
    Label(b,text='Enter password',font=('roman 15 bold'),bg='light green',pady=5,padx=5).grid(row=0,column=0)
    Label(b,text='ATM number',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=1,column=0)
    Label(b,text='Enter amount',font=('roman 15 bold'),pady=5,padx=5,bg='light green').grid(row=2,column=0)
    aaa=Entry(b,textvariable=password1)
    aaa.grid(row=0,column=1)
    aab=Entry(b,textvariable=atmnumber)
    aab.grid(row=1,column=1)
    aac=Entry(b,textvariable=amount1)
    aac.grid(row=2,column=1)
    def tom():
        aq=f"{aaa.get()}"
        bs=f"{aab.get()}"
        af=f"{aac.get()}"
        z=int(af)
        x=open(bs+aq,'r')
        h=x.read()
        f=int(h)
        cvb=z+f
        gh=str(cvb)
        xa=open(bs+aq,'w')
        xa.write(gh)
        tsmg.showinfo("Me Bank",f"Amount in your account after this deposit is {gh}")
        b.destroy()
    Button(b,text='submit',command=tom).grid(row=3,column=1)

def account():
    b=Frame(a_root,bg='light green',borderwidth=10,relief='sunken')
    b.pack(side='right',fill='y')
    password1=StringVar()
    atmnumber=StringVar()
    Label(b,text='Enter password',font=('roman 15 bold'),bg='light green',pady=5,padx=5).grid(row=0,column=0)
    Label(b,text='ATM number',font=('roman 15 bold'),bg='light green',pady=5,padx=5).grid(row=1,column=0)
    aaa=Entry(b,textvariable=password1)
    aaa.grid(row=0,column=1)
    aab=Entry(b,textvariable=atmnumber)
    aab.grid(row=1,column=1)
    
    def sod():
        rt=f"{aaa.get()}"
        zo=f"{aab.get()}"
        
        x=open(zo+rt,'r')
        h=x.read()
        tsmg.showinfo("Me Bank",f"Amount in your account is {h}")
        b.destroy()
    Button(b,text='submit',command=sod).grid(row=2,column=1)


Label(a,text='Create Account',font=('roman 20 bold'),pady=5,padx=5,bg='skyblue').pack()
Button(a,text='Create Account',command=password).pack()

Label(a,text='Account Holder',font=('roman 20 bold'),pady=5,padx=5,bg='skyblue').pack()
Button(a,text='Withdraw Amount',command=withdraw).pack()
Button(a,text='Deposit Money',command=deposit).pack()
Button(a,text='Account History',command=account).pack()
a_root.mainloop()