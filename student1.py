#1.Creating Window
from tkinter import*


root=Tk()

#7.creating functions
def Student_Details():
    name=Name.get()
    S_Name.set(name)
    rollnumber=Rollnumber.get()
    S_number.set(rollnumber)
    phonenumber=Phonenumber.get()
    S_phonenumber.set(phonenumber)
    email=Email.get()
    S_email.set(email)
    branch=Branch.get() 
    S_branch.set(branch) 
    section=Section.get()
    S_section.set(section)
    address=Address.get()
    S_address.set(address)



    java_marks=float(Java.get())
    S_javamarks.set(java_marks)
    dotnet_marks=float(Dotnet.get())
    S_dotnetmarks.set( dotnet_marks)
    webdevelopment_marks=float(Web.get())
    S_webdevelopmentmarks.set(webdevelopment_marks)
    database_marks=float(Database.get())
    S_databasemarks.set(database_marks)
    python_marks=float(Python.get())
    S_pythonmarks.set(python_marks)
    total=java_marks+dotnet_marks+webdevelopment_marks+database_marks+python_marks
    Total_marks.set(total)
    average=total/5
    Average_marks.set(average)
    
    
    
    

    if java_marks < 35 or dotnet_marks < 35 or webdevelopment_marks< 35 or database_marks< 35 or python_marks < 35:
        Grade.set("Fail")
        status = "Fail"
        Status.set(status)
    elif average >= 90:
        Grade.set("A")
        status = "Pass"
        Status.set(status)
    elif average>= 80:
        Grade.set("B")
        status = "Pass"
        Status.set(status)
    elif average>= 70:
        Grade.set("C")
        status = "Pass"
        Status.set(status)
    else:
        Grade.set("Pass")
        status = "Pass"
        Status.set(status)
    
 
 

#2.Creating window size and title
root.title("GUI Student_Details")
root.geometry("1000x600")
S_Name = StringVar()
S_number=StringVar()
S_phonenumber=StringVar()
S_email=StringVar()
S_branch=StringVar()
S_section=StringVar()
S_address=StringVar()
S_javamarks=StringVar()
S_dotnetmarks=StringVar()
S_webdevelopmentmarks=StringVar()
S_databasemarks=StringVar()
S_pythonmarks=StringVar()
Total_marks=StringVar()
Average_marks=StringVar()
Grade = StringVar()
Status = StringVar()
#3.Creating window labels
Label(root,text="Enter Student Name:").grid(row=0,column=0)
Label(root,text="Enter Student Roll Number:").grid(row=1,column=0)
Label(root,text="Enter Student Phone Number:").grid(row=2,column=0)
Label(root,text="Enter Student Email ID:").grid(row=3,column=0)
Label(root,text="Enter Student Branch:").grid(row=4,column=0)
Label(root,text="Enter Student Section:").grid(row=5,column=0)
Label(root,text="Enter Student Address:").grid(row=6,column=0)
Label(root,text=" ").grid(row=7,column=0)
Label(root,text="Enter Student Java Marks:").grid(row=8,column=0)
Label(root,text="Enter Student Dot Net Marks:").grid(row=9,column=0)
Label(root,text="Enter Student Web Development Marks:").grid(row=10,column=0)
Label(root,text="Enter Student Dtabase Marks:").grid(row=11,column=0)
Label(root,text="Enter Student Python Marks:").grid(row=12,column=0)

#4.Creating text boxes
Name= Entry(root)
Name.grid(row=0,column=1)
Rollnumber= Entry(root)
Rollnumber.grid(row=1,column=1)
Phonenumber=Entry(root)
Phonenumber.grid(row=2,column=1)
Email= Entry(root)
Email.grid(row=3,column=1)
Branch= Entry(root)
Branch.grid(row=4,column=1)
Section= Entry(root)
Section.grid(row=5,column=1)
Address= Entry(root)
Address.grid(row=6,column=1)

Java= Entry(root)
Java.grid(row=8,column=1)
Dotnet= Entry(root)
Dotnet.grid(row=9,column=1)
Database= Entry(root)
Database.grid(row=10,column=1)
Web= Entry(root)
Web.grid(row=11,column=1)
Python= Entry(root)
Python.grid(row=12,column=1)

#5.Creating a button for submitting

Button(root,text="Submit", command=Student_Details).grid(row=14,column=1)


#6.Result
Label(root, text="Student Name:",).grid(row=16, column=0)
Label(root, text="", textvariable=S_Name).grid(row=16, column=1)
Label(root, text="Student Roll No:",).grid(row=16, column=2)
Label(root, text="", textvariable=S_number).grid(row=16, column=3)
Label(root, text="Student Phone Number:",).grid(row=16, column=4)
Label(root, text="", textvariable=S_phonenumber).grid(row=16, column=5)
Label(root, text="Student Email ID:",).grid(row=17, column=0)
Label(root, text="", textvariable=S_email).grid(row=17, column=1)
Label(root, text="Student Branch:",).grid(row=17, column=2)
Label(root, text="", textvariable=S_branch).grid(row=17, column=3)
Label(root, text="Student Section:",).grid(row=17, column=4)
Label(root, text="",textvariable=S_section).grid(row=17, column=5)
Label(root, text=" Student Address:", ).grid(row=18, column=0)
Label(root, text="", textvariable=S_address).grid(row=18, column=1)
Label(root, text="Student Java Marks", ).grid(row=19, column=0)
Label(root, text="", textvariable=S_javamarks).grid(row=19, column=1)
Label(root, text="Student Dot Net Marks", ).grid(row=19, column=2)
Label(root, text="", textvariable=S_dotnetmarks).grid(row=19, column=3)
Label(root, text="Student Web Development Marks:", ).grid(row=19, column=4)
Label(root, text="", textvariable=S_webdevelopmentmarks).grid(row=19, column=5)
Label(root, text="Student Database Marks:", ).grid(row=20, column=0)
Label(root, text="",textvariable=S_pythonmarks ).grid(row=20, column=1)
Label(root, text="Python Marks", ).grid(row=20, column=2)
Label(root, text="", textvariable=S_pythonmarks).grid(row=20, column=3)
Label(root, text="---------------Student Total Marks And Average---------", ).grid(row=22, column=0)
Label(root, text="Student Total Marks:", ).grid(row=24, column=0)
Label(root, text="", textvariable=Total_marks).grid(row=24, column=1)
Label(root, text="Student Average Marks:", ).grid(row=25, column=0)
Label(root, text="", textvariable=Average_marks).grid(row=25, column=1)
Label(root, text="Student Grade Marks:", ).grid(row=27, column=0)
Label(root, text="", textvariable=Grade).grid(row=27, column=1)

Label(root, text="Student Status:", ).grid(row=29, column=0)
Label(root, text="", textvariable=Status).grid(row=29, column=1)


mainloop()