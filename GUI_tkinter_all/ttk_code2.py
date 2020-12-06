import tkinter as tk
import tkinter.ttk as ttk

class GUI:
    def __init__(self, master):
        master.geometry('900x800')
        master.title('Sample Messagebox')

        self.notebook = ttk.Notebook(master, width=400, height=400)

        self.frame_students = ttk.Frame(self.notebook)
        self.frame_teachers = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_students, text='Students')
        self.notebook.add(self.frame_teachers, text='Teachers')

        self.notebook.bind('<<NotebookTabChanged>>', self.tab_changed_handler)

        self.frame_students.label_name = ttk.Label(self.frame_students, text='Adı Soyadı')
        self.frame_students.label_name.grid(row=0, column=0, pady=(20,10))
        self.frame_students.entry_name = ttk.Entry(self.frame_students)
        self.frame_students.entry_name.grid(row=0, column=1, pady=(20,10))

        self.frame_teachers.radio1 = ttk.Radiobutton(self.frame_teachers, text='Fizik')
        self.frame_teachers.radio1.grid(row=0, column=0)

        self.frame_teachers.radio2 = ttk.Radiobutton(self.frame_teachers, text='Kimya')
        self.frame_teachers.radio2.grid(row=0, column=1)

        self.frame_teachers.radio3 = ttk.Radiobutton(self.frame_teachers, text='Matematik')
        self.frame_teachers.radio3.grid(row=0, column=2)

        self.frame_teachers.radio4 = ttk.Radiobutton(self.frame_teachers, text='Biyoloji')
        self.frame_teachers.radio4.grid(row=0, column=3)

        self.button_ok = ttk.Button(master, text='Ok', command=self.button_ok_handler)
        self.notebook.pack()
        self.button_ok.pack()

    def button_ok_handler(self):
        #self.notebook.hide(self.frame_students)
        self.notebook.select(1)
        #self.notebook.tab(0, text='xxxxx')

    def tab_changed_handler(self, event):
        print('Tab changed')

root = tk.Tk()
gdb = GUI(root)
root.mainloop()