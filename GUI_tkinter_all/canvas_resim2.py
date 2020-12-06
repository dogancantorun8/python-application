import tkinter as tk
from PIL import Image
from PIL import ImageTk


#taşıma işlemi yaptım ve arka tarafta herhangi bir etki bırakmadım.
class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('Sample Messagebox')

        #ilk konumlandırmalarım icin tanımladıgım degiskenlerim
        self.IMAGE_INIT_X = 300
        self.IMAGE_INIT_Y = 200

        #abbey road resmimi oluşturdum
        img = Image.open('abbey_road.jpg')
        img = ImageTk.PhotoImage(img)
        #resmin boyutlarını değişkene aldım
        self.image_width = img.width()
        self.image_height = img.height()


        #image çizdirmek icin yazdıgım blok
        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.img = img
        self.image_id = self.canvas.create_image(self.IMAGE_INIT_X, self.IMAGE_INIT_Y, image=img) #canvas id ile yarattıgım sekli saklıyorum create line vs içinde id oluşturma işlemi aynıdır

        # x.pos ve y.pos değişkenleri imagenin köşe koordinatlarını tutuyor
        self.xpos = self.IMAGE_INIT_X - self.image_width / 2
        self.ypos = self.IMAGE_INIT_Y - self.image_height / 2

        #hareketin basladıgını gösteren flag degerim 
        self.move_flag = False


        self.canvas.bind('<Button-1>', self.mouse_click_handler)
        self.canvas.bind('<B1-Motion>', self.mouse_motion_handler)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_release_handler)

        self.canvas.pack(fill='both', expand=True)

    #ilk mouse a tıklanıldığı andan tetiklenen fonksiyonum
    def mouse_click_handler(self, event):
        if event.x > self.xpos and event.x < self.xpos + self.image_width and event.y > self.ypos and event.y < self.ypos + self.image_height:

            #eventin bittigi yerdeki koordinatları seklin koordinatlarına atıyorum
            self.prevx = event.x
            self.prevy = event.y

            self.move_flag = True

    #mouse a basılı oduğu andaki handler
    def mouse_motion_handler(self, event):
        if self.move_flag:
            deltax = event.x - self.prevx
            deltay = event.y - self.prevy

            self.canvas.move(self.image_id, deltax, deltay)

            #x.pos ve y.pos değişkenleri tasıma isleminden sonra güncelleniyor
            self.xpos += deltax
            self.ypos += deltay

            self.prevx = event.x
            self.prevy = event.y

    #mousedan elimizi çektiğimizde yakalayan handler
    def mouse_release_handler(self, event):
        self.move_flag = False

root = tk.Tk()
gdb = GUI(root)
root.mainloop()
