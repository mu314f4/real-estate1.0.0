#usr/bin/python

number = 0

from tkinter import*
from tkinter import messagebox
import os 

window = Tk()
window.title('languge-selection')
window.iconbitmap('favicon.ico')
window.geometry('450x250+550+180')
window.minsize(200,300)
window.maxsize(500,500)
window.config(bg='black')

def printer():
	A = Label(window,text='İf you can understand english better than turkish then choise  english.',fg='green',font='Arial 10 bold',bg='black');A.pack()
	B = Label(window,text='Eğer türkçeyi ingilizceden daha  iyi anlıyorsan türkçe yi  seç.',fg='green',font='Arial 10 bold',bg='black');B.pack()
	C = Label(window,text='İf you choise turkish then you cannot adjust with that program.',fg='green',font='Arial 10 bold',bg='black');C.pack()
	D = Label(window,text='Eğer ingilizceyi seçersen bu uygulamadan daha türkçe seçemezsin',fg='green',font='Arial 10 bold',bg='black');D.pack()
	E = Label(window,text="for english click: e or E",fg='green',font='Arial 10 bold',bg='black');E.pack()
	F = Label(window,text="Türkçe  için: T   veya  t",fg='green',font='Arial 10 bold',bg='black');F.pack()
printer()

def c():
	if C.get() == 'ENGLISH':
		os.system('py english.py')
		window.destroy()
		exit()
	elif C.get() == 'TÜRKÇE':
		os.system('py turkce.py')
		window.destroy()
		exit()
	else:
		global number
		number+=1
		if number==3:
			messagebox.showinfo(title='Language Info',message='Fucking man You just Could chose an language for continue\nLanet olasıcık alttarafı bir dil seçeceksin')
			number = 0
		else:	
			messagebox.showinfo(title='Language Info',message='You Should chose an language for continue\nDevam etmek için bir dil seçmelisiniz')

C = StringVar()
C.set('Choise-Seç')
d = OptionMenu(window,C,'ENGLISH','TÜRKÇE')
d.pack(pady=50)

buton = Button(window,text='Confirm/Onayla',activebackground='yellow',font='Vergana 15 underline',activeforeground='purple',fg='red',bg='black',command=c);buton.pack()

window.mainloop()