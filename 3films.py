
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import csv

# Project is not finished, it only forms base
# base.csv file needed as it has headers 

x = 'Виберіть фільм, \n надайте йому свою оцінку\n та напишіть про нього кілька слів'

def get2box():
	
	with open('base.csv', 'a', newline='') as base:
		noteform=Textb.get('1.0','end').rstrip()
		
		if noteform == "":
			noteform = 'Користувач не залишив коментар'
		line=  [Combo1.get(), noteform, Combo2.get() ]
		recorder = csv.writer(base)
		recorder.writerow(line)


	Screen.config(text='Чудовою Залиште відгуки і про інші фільми')

def printfilms():
	
	with open ('base.csv', ) as base:
		recorder = csv.DictReader(base)
		dic = [{"film_name":row['film_name'], 'note':row['note'], 'rating':row['rating']}for row in recorder]
		print(dic)
		
def count_average():
	with open ('base.csv', ) as base:
		findict={}
		for i in tuplefilms:
			findict[i]=[]
		
		recorder = csv.DictReader(base)
		diclist = [{"film_name":row['film_name'], 'note':row['note'], 'rating':row['rating']}for row in recorder]
		for dic in diclist:
			findict[dic['film_name']].append(dic['rating'])
		print(findict)
		




tuplefilms = ('Поводир', 'Фортеця Хаджибей', 'Черкаси', 'Вечір на Івана Купала', 'Легенда про княгиню Ольгу', 'Гуцулка Ксеня ', 'Стоп-Земля', 'Пригоди S Миколая ', 'Сватання на Гончарівці ')
tuplerate = (1,2,3,4,5)


root = Tk()
root.title("Тека фільмів")
root.geometry("800x850")

starfont = Font(
	family="Helvetica",
	size=14,
	weight='bold',
	slant='roman',
	underline=0,
	overstrike=0)

frame = Frame(root, bg="red")

Combo1 = ttk.Combobox(root , values = tuplefilms)
Combo1.set("Оберіть фільм")

Combo2 = ttk.Combobox(root , values = tuplerate)
Combo2.set("Залиште оцінку")
Screen = Label(root, text = x, bg='#a2fab2', font=starfont, padx=4, pady=2, borderwidth=5, width=40, height = 5 )
Button1 = Button(root, text = 'Оцінити >>', font=starfont, width=30, height = 4, borderwidth=2, padx=2, pady=2, bg='#6cf084', command=get2box)
Button2 = Button(root, text = 'Фільми в консоль >>', font=starfont, width=30, height = 3, borderwidth=2, padx=2, pady=2, bg='#6cf084', command=printfilms)
Button3 = Button(root, text = 'Count rate not ready >>', font=starfont, width=30, height = 3, borderwidth=2, padx=2, pady=2, bg='#6cf084', command=count_average)
Textb=Text(root, height=8)

frame.grid(row=0, column=0, columnspan=3, rowspan=8)
Combo1.grid(row=0, column=0, columnspan=1, padx = 10, pady = 20)
Combo2.grid(row=1, column=0, columnspan=1, padx = 10, pady = 20)
Button1.grid(row=3, column=0, columnspan=2, padx = 20, pady = 20)
Screen.grid(row=4, column=0, padx=10, pady=10, columnspan=1)
Textb.grid(row=5, column=0, padx = 20, pady = 20)
Button2.grid(row=7, column=0, columnspan=1, padx = 20, pady = 20)
Button3.grid(row=8, column=0, columnspan=1, padx = 20, pady = 10)


root.mainloop()


