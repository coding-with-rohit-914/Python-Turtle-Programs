from tkinter import *
class StudentsData:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x800')
        title1 = Label(self.root, text='Welcome To NTH Students Information.', font=('cooper black',40),
                      bg='blue', fg='orange', bd=5, relief='raised')
        title1.pack(fill='x')

        dataEntryFrame = Frame(self.root, width=400, height=700, bg=('#BCEE68'))
        dataEntryFrame.place(x=10, y=80)

        dataDisplayFrame = Frame(self.root, width=1070, height=700, bg='#76EEC6')
        dataDisplayFrame.place(x=420, y=80)