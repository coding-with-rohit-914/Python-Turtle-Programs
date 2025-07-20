from tkinter import *

class StudentsData:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x800')
        title1 = Label(self.root, text='Welcome To NTH Students Information', font=('cooper black',40),
                      bg='green', fg='white', bd=5, relief='raised')
        title1.pack(fill='x')

        dataEntryFrame = Frame(self.root, width=400, height=700, bg='green')
        dataEntryFrame.place(x=10, y=80)

        dataDisplayFrame = Frame(self.root, width=1070, height=700, bg='green')
        dataDisplayFrame.place(x=420, y=80)

        #Working on DataEntryFrame
        title2 = Label(self.root, text='Please Enter Data Here!!!', font=('cooper black',15),
                      bg='green', fg='white', bd=5, relief='raised')
        title2.place(x=60, y=85)

        #Roll Number
        rollnoLb1 = Label(dataEntryFrame, text='Roll No:', font=('constantia',15),bg='green',fg='white', bd=5, relief='raised')
        rollnoLb1.place(x=10, y=60)

        rollnoEntry = Entry(dataEntryFrame,font=('constantia',15))
        rollnoEntry.place(x=130, y=65) #170/60

        #First Name
        fnameLb1 = Label(dataEntryFrame, text='First Name:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        fnameLb1.place(x=10,y=100) #110

        fnameEntry = Entry(dataEntryFrame,font=('constantia',15))
        fnameEntry.place(x=130,y=105) #170/110

        #Last Name
        LnameLb1 = Label(dataEntryFrame, text='Last Name:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        LnameLb1.place(x=10,y=140)

        LnameEntry = Entry(dataEntryFrame,font=('constantia',15))
        LnameEntry.place(x=130,y=145)
        
        #Email ID
        EmailIDLb1 = Label(dataEntryFrame, text='Email ID:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        EmailIDLb1.place(x=10,y=180)

        LnameEntry = Entry(dataEntryFrame,font=('constantia',15))
        LnameEntry.place(x=130,y=185)
    
        #Mobile Number
        MobileNoLb1 = Label(dataEntryFrame, text='Mobile No:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        MobileNoLb1.place(x=10,y=220)

        MobileNoEntry = Entry(dataEntryFrame,font=('constantia',15))
        MobileNoEntry.place(x=130,y=225)
        
        #Course Name
        CourseNameLb1 = Label(dataEntryFrame, text='Course:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        CourseNameLb1.place(x=10,y=260)

        CourseNameEntry = Entry(dataEntryFrame,font=('constantia',15))
        CourseNameEntry.place(x=130,y=265)
       
        #Fee
        FeeLb1 = Label(dataEntryFrame, text='Fee:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        FeeLb1.place(x=10,y=300)

        FeeEntry = Entry(dataEntryFrame,font=('constantia',15))
        FeeEntry.place(x=130,y=305)
        
        #Institute Name
        InstituteNameLb1 = Label(dataEntryFrame, text='Institute:', font=('constantia',15),bg='green', fg='white', bd=5, relief='raised')
        InstituteNameLb1.place(x=10,y=340)

        InstituteNameEntry = Entry(dataEntryFrame,font=('constantia',15))
        InstituteNameEntry.place(x=130,y=345)

root = Tk()

obj = StudentsData(root)