import time
import webbrowser
import tkinter as tk
import subprocess

def happyend():
    btn_yes.config(text='Вас взяли в плен,Украина пала через 2 минуты после этого\nДень вашего плена объявлен главным праздником в РФ\nУкраина перешла под контроль РОССИЙСКОЙ ФЕДЕРАЦИИ',height=1920,width=1080,font="Times 50",command=zelyavict)
    
def lomka():
    lable.config(text='У вас началась\nочень сильная ломка\nнадо что-то сделать')
    btn_yes.config(text='Сдаться в плен и получить дозу коки',command=happyend)
    btn_no.config(text='Завершить жизнь\nсуидцидом',command=end)
def zelyalose():
    lable.config(text="Украина переходит в состав Рф\n Выберите следующего\nпрезидента",width=40,height= 20,font='Times 14')
    btn_yes.config(text='Никита Zov Васильевич',height=30 ,width= 30,bg='green' ,command=zelyavict)
    btn_no.config(text='Эдуард Svoi Жданов',height=30, width= 30,bg='green',command=zelyavict)

def titles():
    subprocess.call('titles.mp4',shell=True)

def zelyavict():
    lable.config(text="Украина процветает\nИгра окончена.",font='Times 20',bg='Green')
    btn_yes.config(text="Выйти из игры",font='Times 25', width=30, height=10,command=root.destroy)
    btn_no.config(text="Титры",font='Times 25', width=30, height=10,activebackground='Green',bg='green',command=titles) 


def svo():
    root.destroy()
    webbrowser.open("https://ria.ru/20220622/spetsoperatsiya-1795199102.html")
def es():
    lable.config(text='Ваши действия\nповлекли начало СВО.\nРАсход кокаина увеличился',font="Times 17")
    btn_no.config(text='Попросить у Бiдена', width=15, height=1, bg='Red', command=ask_biden)
    btn_yes.config(text='Сдать харькiв', command=end)

def ask_biden():
    lable.config(text='Выйграл Трамп\n(Бiдона бiльше немаэ)',font="Times 17")
    btn_no.config(text='Подпiсать 28 пунктов\n(Capituliren)', width=15, height=1, bg='Red', command=zelyalose)
    btn_yes.config(text='Завязать с коксом', command=lomka)


def putin_bro():
    lable.config(text='Путин настаивает на\nприсоединении Украины\nв состав РФ',font="Times 17")
    btn_yes.config(text='Перейти в состав\nРФ', bg='Green', width=60, height=30, fg='White', command=zelyavict)
    btn_no.config(text='Попытаться отстоять\nнезависимость', width=16, height=2, bg='Red', command=svo)

def end():
    root.destroy()
    daun = command=webbrowser.open("https://funny.klev.club/uploads/posts/2024-03/funny-klev-club-p-smeshnie-kartinki-pro-zelenskogo-i-prikoln-6.jpg")
    time.sleep(2)
    subprocess.call('titles.mp4',shell=True)

def daun():
    root.destroy()
    daun = command=webbrowser.open("https://pikuco.ru/tests/49987/")
    time.sleep(3)
    daun=command=webbrowser.open("https://s0.rbk.ru/v6_top_pics/media/img/4/20/754899888059204.jpg")
def nenachalo():
    lable.config(text="Ты точно не хочешь?",font="Times 17")
    btn_no.config(text="Точно нет!!!",width=15,height=1,font="Times 10",bg='red',command=daun)
    btn_yes.config(text="Ладно,хочу!!!",command=begin_svo)
def new_win():
    lable.config(text="Кого поставить \nновым президентом?",font='Times 17')
    btn_yes.config(text="Эдуарда ZOV Жданова",font='Times 25', width=30, height=30)
    btn_no.config(text="Никиту SVOI Васильевича",font='Times 25', width=30, height=30,activebackground='Green')

def coca():
    root.destroy()
    coca = command=webbrowser.open("https://news.mail.ru/politics/68854731/")
    time.sleep(5)
    coca = command=webbrowser.open("https://dailystorm.ru/news/zelenskiy-odel-kipu-i-pomolilsya-u-steny-placha-v-ierusalime")

def vict():
    lable.config(text='ПОБЕДА',font="Times 25")
    btn_yes.config(text='ZOV',width=30, height=10, fg='White',command=new_win)
    btn_no.config(text='ЗОВ', bg='Green', width=30, height=10, fg='White',command=new_win)

def bomb():
    lable.config(text='Вы захватили Зеленского',font="Times 17")
    btn_yes.config(text='Убить', command=vict)
    btn_no.config(text='Дать кокаина', width=15, height=1, bg='Red',command=coca)

def begin_svo():
    lable.config(text='Что разбомбить?',font="Times 25")
    btn_yes.config(text='Детский дом', bg='Green', width=60, height=30, fg='White', command=bomb)
    btn_no.config(text='Больница для детей', bg='Green', width=60, height=30, fg='White',font='Times 15', command=bomb)



root = tk.Tk()
root.title("СИМУЛЯТОР ПОЛИТИКИ")
root.geometry("1920x1080")

putin_image = tk.PhotoImage(file='777.png')
zelensky_image = tk.PhotoImage(file='000.png')
loading = tk.PhotoImage(file='loading.png')
#z_end_image = tk.PhotoImage(file='loading.png')

bg_lable = tk.Label(root, image=loading)
bg_lable.place(x=0, y=0, relwidth=1, relheight=1)

lable = tk.Label(root, bg='Gray', text='Выберите\nперсонажа',font="Times 25", fg='White')
lable.place(x=800, y=470, width=250, height=150)

def putin():
    bg_lable.config(image=putin_image)
    lable.config(text='Начать СВО?',font="Times 25")
    btn_yes.config(text='Да!!!!', bg='Green', width=60, height=30, fg='White', command=begin_svo)
    btn_no.config(text='Не хочу!!!', bg='Green', width=60, height=30, fg='White',font='Times 15', command=nenachalo)
def zelensky():
    bg_lable.config(image=zelensky_image)
    lable.config(text='ЕС\nили\nПутин братишка',font="Times 25")
    btn_yes.config(text='Путин братишка', bg='Green', width=50, height=10, fg='White', command=putin_bro)
    btn_no.config(text='ЕС', bg='Red', width=30, height=10, fg='White',font='Times 15', command=es)



btn_yes = tk.Button(root, text="Путин", width=60, height=30, bg='Green', fg='White', activebackground='Green',font='Times 15', command=putin)
btn_yes.pack(side='right')


btn_no = tk.Button(root, text="Зеленский", width=60, height=1, bg='Red',font='Times 15',command=zelensky)
btn_no.pack(side='left')

root.mainloop()
