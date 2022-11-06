import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
class NewsApp:

    def __init__(self):
        #fetch data
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=6fb9849ef9b5482f82315ece993f8249').json()
        #print(self.data)
        #initial gui load
        self.load_gui()

        #load the first news item
        self.load_news_items(0)


    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title("My new app")
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_items(self,idx):
        #clear the screen for the new news item
        self.clear()

        try:
            img_url = self.data['articles'][idx]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://demofree.sirv.com/nope-not-here.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)




        label=Label(self.root,image=photo)
        label.pack()

        heading=Label(self.root,text=self.data['articles'][idx]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][idx]['description'], bg='black', fg='white', wraplength=350,
                        justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame=Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if idx!=0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_items(idx - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][idx]['url']))
        read.pack(side=LEFT)

        if idx!=len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_items(idx + 1))
            next.pack(side=LEFT)




        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

obj=NewsApp()