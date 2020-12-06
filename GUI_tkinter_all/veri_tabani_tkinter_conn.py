import tkinter as tk
import sqlite3

#bu kodda ögrenci adı ve numarasıyla  consoledan kayıt islemi yapacagım

import tkinter as tk
import sqlite3

class GUIDatabase:
   def __init__(self, master): #root self yerine geciyor
       self.master = master
       master.geometry('360x180')
       master.resizable(width=False,height=False) #en dıs pencerenin boyutları degistirilemez
       master.title('Database GUI Example')
       self.conn = sqlite3.connect('student.sqlite')
       cur = self.conn.cursor()
       cur.execute("CREATE TABLE IF NOT EXISTS student(student_no INTEGER PRIMARY KEY, student_name TEXT)")

       self.label_name = tk.Label(master, text='Adı Soyadı:', font='Calibri 12')
       self.label_name.place(x=10, y=10)
       self.entry_name = tk.Entry(master, width=30, font='Calibri 12')
       self.entry_name.place(x=10, y=35)

       self.label_no = tk.Label(master, text='No:', font='Calibri 12')
       self.label_no.place(x=10, y=65)
       #veri aldıgm labeller yaratıyorum
       self.entry_no = tk.Entry(master, width=20, font='Calibri 12')
       self.entry_no.place(x=10, y=90)

       self.button_record = tk.Button(master, text='Kaydet', command=self.record)
       self.button_record.place(x=175, y=125, width=70, height=30)

       self.button_close = tk.Button(master, text='Çıkış', command=self.master.quit) #root widgetinin quit methoduyla cıkıs sagladım
       self.button_close.place(x=270, y=125, width=70, height=30)


       cur.close()

       self.entry_name.focus() #klavye odagını ilk labela cektim

   def record(self):
      try:
         name = self.entry_name.get().strip()
         no = int(self.entry_no.get().strip())

         cur = self.conn.cursor()
         cur.execute("INSERT INTO student VALUES(?, ?)", (no, name)) #dbde yapmak istedigim islemi cur nesneme yaptırdım
         self.conn.commit() #self nesnemi dbye commit ediyorum
         cur.close()


         self.entry_name.delete(0, tk.END) #kayıttan sonra fieldleri bosalttım
         self.entry_no.delete(0, tk.END)
         self.entry_name.focus()  # klavye odagını ilk fielda cektim

      except sqlite3.Error as e:
         print(e)


root = tk.Tk()
gdb = GUIDatabase(root)
root.mainloop()