import pymem #line:1
import pymem .process #line:2
import requests #line:3
from threading import Thread #line:4
print ('>>> Запускается чит...')#line:8
pm =pymem .Pymem ("csgo.exe")#line:10
client =pymem .process .module_from_name (pm .process_handle ,"client.dll").lpBaseOfDll #line:11
print ('')#line:13
print ('>>> Получение оффсетов...')#line:14
offsets ='https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'#line:16
response =requests .get (offsets ).json ()#line:17
dwGlowObjectManager =int (response ["signatures"]["dwGlowObjectManager"])#line:19
dwEntityList =int (response ["signatures"]["dwEntityList"])#line:20
m_iTeamNum =int (response ["netvars"]["m_iTeamNum"])#line:22
m_iGlowIndex =int (response ["netvars"]["m_iGlowIndex"])#line:23
print ('>>> Запуск WallHack...')#line:25
def ESP ():#line:27
    while True :#line:28
        O0O000OO0O00OO000 =pm .read_int (client +dwGlowObjectManager )#line:29
        for OOOO00OO0O0OOOO0O in range (1 ,32 ):#line:31
            OOO0000000OO000O0 =pm .read_int (client +dwEntityList +OOOO00OO0O0OOOO0O *0x10 )#line:32
            if OOO0000000OO000O0 :#line:34
                O0OO00OO00O0O00O0 =pm .read_int (OOO0000000OO000O0 +m_iTeamNum )#line:35
                OOO0O00OO000O0O0O =pm .read_int (OOO0000000OO000O0 +m_iGlowIndex )#line:36
                if O0OO00OO00O0O00O0 ==2 :#line:38
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x4 ,float (1 ))#line:39
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x8 ,float (0 ))#line:40
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0xC ,float (1 ))#line:41
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x10 ,float (1 ))#line:42
                    pm .write_int (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x24 ,1 )#line:43
                elif O0OO00OO00O0O00O0 ==3 :#line:45
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x4 ,float (1 ))#line:46
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x8 ,float (0 ))#line:47
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0xC ,float (1 ))#line:48
                    pm .write_float (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x10 ,float (1 ))#line:49
                    pm .write_int (O0O000OO0O00OO000 +OOO0O00OO000O0O0O *0x38 +0x24 ,1 )#line:50
Thread (target =ESP ).start ()#line:52
print ('>>> Чит запущен.')