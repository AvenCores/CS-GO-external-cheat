import subprocess

version = 1.0

def wallhack():
    subprocess.call('start /wait python wh mod.py', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def bhop():
    subprocess.call('start /wait bhop mod.py', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def RadarHack():
    subprocess.call('start /wait radarhack mod', shell=True)
    global banner
    print(banner+"\nНажмите ENTER для выхода в главное меню")
    input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
 _____      _                         _        _                _
| ____|_  _| |_ ___  _ __ _ __   __ _| |   ___| |__   ___  __ _| |_
|  _| \ \/ / __/ _ \| '__| '_ \ / _` | |  / __| '_ \ / _ \/ _` | __|
| |___ >  <| ||  __/| |  | | | | (_| | | | (__| | | |  __/ (_| | |_
|_____/_/\_\\__\____ |_|  |_| |_|\____|_|  \___|_| |_|\___|\__,_|\__|

Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """
    print(banner)
    menu = input('1 - Запустить WallHack\n2 - Запустить Bhop\n3 - Запустить RadarHack\n\n4 - Важная информация!\n\n0 - Выход\n')
    if menu == "0": exit()
    if menu == "1": wallhack()
    if menu == "2": bhop()
    if menu == "3": RadarHack()
    if menu == "4": info()