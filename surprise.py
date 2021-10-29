from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import random
import pygame as py



# import mp3play
# clip = mp3play.load(r'.\static\Gifty-youngforyou.mp3')
# clip.play()



T = ['房子写你名...','保大...','我妈会游泳...','家务活我干...','工资卡给你...','不要怂!','又不是没那个实力...']

def closeWindow():
    messagebox.showinfo(title="警告", message="关不掉吧，气不气")
    return

def closeallwindow():
    window.destroy()

def love():
    love = Toplevel(window)
    love.geometry("400x130+580+260")
    love.title("")
    label = Label(love, text="我就知道你会同意的哈哈!", font=("楷体", 25))
    label.pack()
    btn = Button(love, text="我个大傻子", width=10, height=2, command=closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)


def closelove():
    messagebox.showinfo(title="好怂啊你", message="喜欢我直说就行")
    return

def noLove():
    tkinter.messagebox.showwarning(title="再想想嘛", message="好怂啊你....")
    tkinter.messagebox.showwarning(title="再想想嘛", message="再考虑考虑嘛...")
    tkinter.messagebox.showwarning(title="再想想嘛", message="过了这村就没这店咯...")

def update(idx):
    frame = frames[idx]
    idx += 1
    label.configure(image=frame)
    window.after(100, update, idx%numIdx)

def callback(event):
    tt = random.randint(0, 6)
    x=random.randint(50, 500)
    y=random.randint(50, 400)
    btn2.place(x=x,y=y,anchor='w')
    label2.config(text=T[tt])

window = Tk()
window.title("来自一个英姿飒爽的小哥哥")
window.geometry("580x460+500+170")
window.protocol("WM_DELETE_WINDOW", closeWindow)
# window['background'] = "#e20909"
label1 = Label(window, text="小姐姐，我观察你很久了！",
               font=("华文行楷", 25), fg="red")
label1.grid()

label2 = Label(window, text="不要怂？", font=("华文行楷", 22))
label2.place(x=350, y=130)
# 图片
numIdx = 3 # gif的帧数
frames = [PhotoImage(file='./static/222.gif', format='gif -index %i' %(i)) for i in range(numIdx)]

label = Label(window)
label.grid(row=2, columnspan=1)
window.after(0, update, 0)

photo = PhotoImage(file="./static/666.gif")
imageLable = Label(window, image=photo)
imageLable.grid(row=2, columnspan=1)

btn1 = Button(window, text="好呀", width=15, height=2, command=love,background="#d1d1d1")
btn1.grid(row=3, column=0, sticky=W)

btn2 = Button(window, text="算了吧", width=15, height=2,background="#d1d1d1", command=noLove)
btn2.grid(row=3, column=1, sticky=E)



btn2.bind("<Enter>",callback)


py.mixer.init()
py.mixer.music.load(r'.\static\Gifty-youngforyou.mp3')
py.mixer.music.play(-1, 0)


window.mainloop()


