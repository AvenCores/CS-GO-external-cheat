import pymem ,requests ,pymem .process #line:1
from threading import Thread #line:2
url ='https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'#line:4
response =requests .get (url ).json ()#line:5
dwLocalPlayer =int (response ["signatures"]["dwLocalPlayer"])#line:7
dwEntityList =int (response ["signatures"]["dwEntityList"])#line:8
m_iTeamNum =int (response ["netvars"]["m_iTeamNum"])#line:10
m_bSpotted =int (response ["netvars"]["m_bSpotted"])#line:11
pm =pymem .Pymem ("csgo.exe")#line:13
client =pymem .process .module_from_name (pm .process_handle ,"client.dll").lpBaseOfDll #line:14
def RadarHack ():#line:16
    while True :#line:17
        if pm .read_int (client +dwLocalPlayer ):#line:18
            O0OO0OOO0O000O0O0 =pm .read_int (client +dwLocalPlayer )#line:19
            O00OO0OO0000OOOO0 =pm .read_int (O0OO0OOO0O000O0O0 +m_iTeamNum )#line:20
            for O000000O0OOOO0000 in range (64 ):#line:21
                if pm .read_int (client +dwEntityList +O000000O0OOOO0000 *0x10 ):#line:22
                    O0OOOOOO000O00OOO =pm .read_int (client +dwEntityList +O000000O0OOOO0000 *0x10 )#line:23
                    OOOOO000O0OOOO0O0 =pm .read_int (O0OOOOOO000O00OOO +m_iTeamNum )#line:24
                    if OOOOO000O0OOOO0O0 !=O00OO0OO0000OOOO0 :#line:25
                        pm .write_int (O0OOOOOO000O00OOO +m_bSpotted ,1 )#line:26
Thread (target =RadarHack ).start ()