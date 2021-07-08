
from tkinter import Tk, Label, Menu
from db import sqlite
import function as fn

app_title = 'first app'
app_size = '300x200'

# Заготовка для запроса
dbcursor = sqlite.cursor()
dbcursor.execute('SELECT * FROM settings')

# Получаем настройки из базы данных
settings = dbcursor.fetchall()

# Начальные настройки для приложения
for config in settings:
    print(config)
    if config[1] == 'title':
        app_title = config[2]
    if config[1] == 'size':
        app_size = config[2]

mainApp = Tk()
mainApp.title(app_title)

# Размер окна width 600px height 300px
mainApp.geometry('600x300')

# flabel = Label(mainApp, text = 'Hello world', font = ('Calibri', 24))
# flabel.grid(column = 30, row = 20)

# Создание главного меню
mainMenus = Menu(mainApp)

fileMenu = Menu(mainMenus, tearoff=0)
fileMenu.add_separator()
fileMenu.add_command(label = 'Настройки')
fileMenu.add_command(label = 'Закрыть', command = fn.exit_program)

productMenu = Menu(mainMenus, tearoff=0)
productMenu.add_command(
    label = 'Добавить',
    command = fn.create_product_window
)
productMenu.add_command(label = 'Список')

mainMenus.add_cascade(label = 'Файл', menu = fileMenu)
mainMenus.add_cascade(label = 'Продукты', menu = productMenu)
mainMenus.add_cascade(label = 'Справка', menu = productMenu)

# Инилизация меню
mainApp.config( menu = mainMenus )
mainApp.mainloop()