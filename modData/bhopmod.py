import pymem #line:1
import pymem .process #line:2
import requests #line:3
from threading import Thread #line:4
import keyboard #line:5
import time #line:6
print ('>>> Запускается чит...')#line:9
pm =pymem .Pymem ("csgo.exe")#line:11
client =pymem .process .module_from_name (pm .process_handle ,"client.dll").lpBaseOfDll #line:12
print ('')#line:14
print ('>>> Получение оффсетов...')#line:16
offsets ='https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'#line:18
response =requests .get (offsets ).json ()#line:19
dwLocalPlayer =int (response ["signatures"]["dwLocalPlayer"])#line:21
dwForceJump =int (response ["signatures"]["dwForceJump"])#line:22
m_fFlags =int (response ["netvars"]["m_fFlags"])#line:24
print ('')#line:26
print ('>>> Запуск BunnyHop...')#line:27
def BunnyHop ():#line:29
    while True :#line:30
        if pm .read_int (client +dwLocalPlayer ):#line:31
            O0000O0O0OO0OOOOO =pm .read_int (client +dwLocalPlayer )#line:32
            OOOO000OO0O000O0O =client +dwForceJump #line:33
            OOOOOOO00OOOOOO00 =pm .read_int (O0000O0O0OO0OOOOO +m_fFlags )#line:34
            if keyboard .is_pressed ("space"):#line:36
                if OOOOOOO00OOOOOO00 ==257 :#line:37
                    pm .write_int (OOOO000OO0O000O0O ,5 )#line:38
                    time .sleep (0.17 )#line:39
                    pm .write_int (OOOO000OO0O000O0O ,4 )#line:40
Thread (target =BunnyHop ).start ()#line:42
print ('')#line:44
print ('>>> BunnyHop запущен.')