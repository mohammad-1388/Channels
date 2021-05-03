import os

def clear():
    if os.name== 'nt':
        os.system("cls")
    else:
        os.system("clear")
        
clear()
os.system("python manage.py runserver 9014")