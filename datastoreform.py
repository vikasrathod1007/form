#import
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql

B=Tk()
#Title
B.title("ADDHAR CARD")

#create Canvas
a=Canvas(B,bg="azure",height=10000,width=10000,scrollregion=(0,0,500,500))
a.pack(expand=YES,fill=BOTH)
#p=PhotoImage(file="flag.png")
#a.create_image(x=700,y=500,image=p,anchor=NW)

#submit
def sub():
    result=messagebox.askokcancel("Confirmation","Do You Want To Submit the Form",icon="question")
    if result is False:
        print("Cancelled")     
    else:
        
        db=mysql.connect(user="root",password="vikas",host='127.0.0.1')
        e=db.cursor()
        ze1=str(ze.get())#referance point
        a1=str(e1.get())#firstname
        b1=e2.get()#middlename
        c1=e3.get()#lastname
        d1=date.get()#dob
        f1=month.get()#dob
        g1=year.get()#dob
        h1=e7.get()#mobile
        I1=e8.get()#e-mail
        l1=e10.get()#room
        m1=e11.get()#street	
        n1=e12.get()#village
        o1=e13.get()#district
        p1=e14.get()#pincode
        r1=e15.get()#city
        q1=e16.get()#state
        s1=e17.get()#country
        t1=var2.get()#disability
        u1=var1.get()#gender
        w1=e15.get()#Qualification
        y1=current.get()#current status
        aa1=str(var10.get())+str(var11.get())+str(var12.get())+str(var13.get())+str(var14.get())+str(var15.get())+str(var16.get())
        
        e.execute("show databases")
        f=e.fetchall()
        for i in range(0,len(f)):
            if "python" in f[i]:
                db_name="".join(f[i])
                break
        e.execute("use "+db_name)
        try:
           e.execute("insert into Addhar_Form values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ze1,a1,b1,c1,d1,f1,g1,h1,I1,l1,m1,n1,o1,p1,r1,q1,s1,t1,u1,w1,y1,aa1))
           db.commit()
           print("Data inserted properly",ze1,"-",a1,"-",b1,"-",c1,"-",d1,"-",f1,"-",g1,"-",h1,"-",I1,"-",l1,"-",m1,"-",n1,"-",o1,"-",p1,"-",r1,"-",q1,"-",s1,"-",t1,"-",u1,"-",w1,"-",y1,"-",aa1)
           print("Submitted")
        except Exception as arg:
           db.rollback()
           db.close()
           print(arg)
           print("Exception occurred")

def mod():
    result=messagebox.askokcancel("Confirmation","Do You Want To Modify the Form",icon="question")
    if result is False:
        print("Cancelled")
    else:
        
        db=mysql.connect(user="root",password="vikas",host='127.0.0.1')
        e=db.cursor()
        e.execute("show databases")
        ze1=ze.get()#referance point
        print(ze)
        a1=e1.get()#firstname
        print(a1)
        b1=e2.get()#middlename
        c1=e3.get()#lastname
        d1=date.get()#dob
        f1=month.get()#dob
        g1=year.get()#dob
        h1=e7.get()#mobile
        I1=e8.get()#e-mail
        l1=e10.get()#room
        m1=e11.get()#street
        n1=e12.get()#village
        o1=e13.get()#district
        p1=e14.get()#pincode
        r1=e15.get()#city
        q1=e16.get()#state
        s1=e17.get()#country
        t1=var2.get()#disability
        u1=var1.get()#gender
        w1=e15.get()#Qualification
        y1=current.get()#current status

        
        f=e.fetchall()
        for i in range(0,len(f)):
            if "python" in f[i]:
                db_name="".join(f[i])
                break
        e.execute("use "+db_name)
        try:
           query="update Addhar_Form set First_Name='%s',Middle_Name='%s',Last_Name='%s',Date='%s', Month='%s', Year='%s', Mobile_No='%s', Email='%s',  Room_No='%s', Street='%s', Village='%s', District='%s', Pincode='%s', City='%s',  State='%s',  Country='%s', Disability='%s', Gender='%s', Qualification='%s', Status='%s' where Id='%s'"%(a1,b1,c1,d1,f1,g1,h1,I1,l1,m1,n1,o1,p1,r1,q1,s1,t1,u1,w1,y1,ze1)
           e.execute(query)
           db.commit()
           print("data updtaed properly",data)
           print("Modified")
        except Exception as arg:
           db.rollback()
           db.close()
           print(arg)
           print("exception occurred")
        


    
#delete        
def delete():
    result=messagebox.askokcancel("Confirmation","Do You Want To Delete the Form",icon="question")
    if result is False:
        print("Cancelled")
    else:
        
        db=mysql.connect(user="root",password="vikas",host='127.0.0.1')
        e=db.cursor()
        ze1=ze.get()
        e.execute("show databases")
        a=e1.get()
        b=e2.get()
        f=e.fetchall()
        for i in range(0,len(f)):
            if "python" in f[i]:
                db_name="".join(f[i])
                break
        e.execute("use "+db_name)
        try:
           query="delete from addhar_form where Id='%s' "%(ze1)
           print(query)
           e.execute(query)
           
           db.commit()
           print("data deleted from table_name")
           
        except Exception as arg:
           db.rollback()
           db.close()
           print("exception occurred")



def Exit():
    B.destroy()


#Header File
l0 = Label(B, text="Aadhar Card Form",font=("Gabriola",50,"bold"),bg="azure")
la = Label(B,text="Personal Details",fg="gray",bg="azure",font=("Gabriola",30,"bold",)).place(x=100,y=90)
l0.place(x=500,y=10)

#Referance
z = Label(B, text="Id No. :",font=("Gabriola",20,"bold"),bg="azure")
z.place(x=135,y=165)
ze = Entry(B ,bd=7)
ze.place(x=220,y=185)

#Name
l1 = Label(B, text="Firstname :",font=("Gabriola",20,"bold"),bg="azure")
l2 = Label(B, text ="Middlename :",font=("Gabriola",20,"bold"),bg="azure")
l3 = Label(B, text ="Lastname :",font=("Gabriola",20,"bold"),bg="azure")
l1.place(x=100,y=205)                    
l2.place(x=400,y=205)
l3.place(x=700,y=205)
e1 = Entry(B ,bd=7)
e2 = Entry(B ,bd=7)
e3 = Entry(B ,bd=7)
e1.place(x=220, y=220)
e2.place(x=540, y=220)
e3.place(x=820, y=220)

#Gender
l5 = Label(B, text ="Gender :",font=("Gabriola",20,"bold"),bg="azure")
l5.place(x=125,y=245)
var1=StringVar()
var1.set(" ")
r1=Radiobutton(B,text="MALE",bg="azure",variable=var1,font=("Gabriola",15),value="MALE")
r2=Radiobutton(B,text="FEMALE",bg="azure",variable=var1,font=("Gabriola",15),value="FEMALE")
r3=Radiobutton(B,text="OTHERS",bg="azure",variable=var1,font=("Gabriola",15),value="OTHERS")
r3.place(x=400,y=250)
r1.place(x=315,y=250)
r2.place(x=220,y=250)

#Date Of Birth
l6 = Label(B, text ="Date Of Birth :",font=("Gabriola",20,"bold"),bg="azure")
l6.place(x=70,y=285)
Date=StringVar()
date=ttk.Combobox(a,width=13,textvariable=Date,font=("Gabriola",10))
date['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
date.current()
date.place(x=220,y=305)

Month=StringVar()
month=ttk.Combobox(a,width=13,textvariable=Month,font=("Gabriola",10))
month['values'] =('January','February','March','April','May','June','July','August'\
            ,'September','October','November','December')
month.current() 
month.place(x=330,y=305)

Year=StringVar()
year=ttk.Combobox(a,width=13,textvariable=Year,font=("Gabriola",10))
year['values']=(1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019)
year.place(x=450,y=305)

#Contact
l7 = Label(B, text ="Mobile No. :",font=("Gabriola",20,"bold"),bg="azure")
l8 = Label(B, text ="Email-ID :",font=("Gabriola",20,"bold"),bg="azure")
l7.place(x=95,y=330)
l8.place(x=400,y=334)
e7 = Entry(B ,bd=7)
e8 = Entry(B ,bd=7)
e7.place(x=230, y=345)
e8.place(x=505, y=345)

#Address
l9 = Label(B, text ="Address :",font=("Gabriola",20,"bold"),bg="azure")
l10 = Label(B, text ="House No. :",font=("Gabriola",20,"bold"),bg="azure")
l11 = Label(B, text ="Street/Road :",font=("Gabriola",20,"bold"),bg="azure")
l12 = Label(B, text ="Village/Town :",font=("Gabriola",20,"bold"),bg="azure")
l13 = Label(B, text ="District :",font=("Gabriola",20,"bold"),bg="azure")
l14 = Label(B, text ="Pin Code :",font=("Gabriola",20,"bold"),bg="azure")
l15 = Label(B, text ="City :",font=("Gabriola",20,"bold"),bg="azure")
l16 = Label(B, text ="State :",font=("Gabriola",20,"bold"),bg="azure")
l17 = Label(B, text ="Country :",font=("Gabriola",20,"bold"),bg="azure")
l9.place(x=120,y=375)
l10.place(x=220,y=375)                    
l11.place(x=500,y=375)
l12.place(x=780,y=375)
l13.place(x=240,y=410)
l14.place(x=525,y=410)
l15.place(x=825,y=410)
l16.place(x=240,y=445)
l17.place(x=530,y=445)

e10 = Entry(B ,bd=7)
e11 = Entry(B ,bd=7)
e10.place(x=350, y=390)
e11.place(x=640, y=390)
e12 = Entry(B ,bd=7)
e13 = Entry(B ,bd=7)
e12.place(x=925, y=390)
e13.place(x=350, y=425)
e14 = Entry(B ,bd=7)
e15= Entry(B ,bd=7)
e14.place(x=640, y=425)
e15.place(x=925, y=425)
e16= Entry(B,bd=7)
e17= Entry(B,bd=7)
e16.place(x=350, y=460)
e17.place(x=640, y=460)

#disability
l_2= Label(B, text ="Person With Disability :",font=("Gabriola",20,"bold"),bg="azure")
l_2.place(x=100,y=495)
var2=StringVar()
var2.set(" ")
rl1=Radiobutton(B,text="Yes",font=("Gabriola",20),variable=var2,value="YES",bg="azure")
rl2=Radiobutton(B,text="No",variable=var2,font=("Gabriola",20),value="NO",bg="azure")
rl1.place(x=350,y=490)
rl2.place(x=420,y=490)

#Qualification
L15=Label(B,text="Qualification  :",font=("Gabriola",20,"bold"),bg="azure")
L15.place(x=150,y=530)
E15=Entry(B ,bd=7)
E15.place(x=300,y=545)

#Current Status
L16=Label(B,text="Current Status :",font=("Gabriola",20,"bold"),bg="azure")
L16.place(x=135,y=570)
Current=StringVar()
current=ttk.Combobox(a,width=13,textvariable=Current,font=("Gabriola",10))
current['values']=('Single','Married','Engaged','Divorced','Widowed','Open Relationship','Other')

current.place(x=300,y=585)

#Atteched Documents
L28=Label(B,bg="azure",text="Attachted Document : ",font=("Gabriola",20,"bold"))
L28.place(x=80,y=615)


var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

C1=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var10,text="Passport",font=("Gabriola",20))
C1.place(x=300,y=615)
C2=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var11,text="PAN card",font=("Gabriola",20))
C2.place(x=470,y=615)
C3=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var12,text="Voter Id",font=("Gabriola",20))
C3.place(x=600,y=615)
C4=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var13,text="Driving Licence",font=("Gabriola",20))
C4.place(x=750,y=615)
C5=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var14,text="Birth Certificate",font=("Gabriola",20))
C5.place(x=300,y=660)
C6=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var15,text="Light Bill",font=("Gabriola",20))
C6.place(x=470,y=660)
C7=Checkbutton(B,bg="azure",onvalue=1,offvalue=0,variable = var16,text="Marksheet",font=("Gabriola",20))
C7.place(x=600,y=660)

#Buttons
b_modify=Button(B,text="UPDATE",font=("Gabriola",15,"bold"),bg="yellow",bd=5,activebackground="azure",activeforeground="red",command=mod)
b_submit=Button(B,text="SUBMIT",font=("Gabriola",15,"bold"),bg="blue",bd=5,activebackground="azure",activeforeground="red",command=sub)
b_delete=Button(B,text="DELETE",font=("Gabriola",15,"bold"),bg="red",bd=5,activebackground="azure",activeforeground="red",command=delete)
b_modify.place(x=450, y=750)
b_submit.place(x=550, y=750)
b_delete.place(x=650, y=750)
b_Exit=Button(B,text="Exit",font=("Gabriola",15,"bold"),bg="grey",bd=5,activebackground="azure",activeforeground="black",command=Exit)
b_Exit.place(x=750,y=750)


#Close Mainloop 
B.mainloop()
