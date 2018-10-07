#website blocker scripts which write to your hosts file, and then deletes entry
#time can be set 

import time 
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.gmail.com","www.mail.google.com", "mail.google.com",
"https://mail.google.com/mail/u/0/"]
#Gmail are sneaky fucks, trouble blocking gmail, even with restart, cookie dump, possibly need a DNS cache flush?

#Set time when you want the website blocker to work on your PC
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,18) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Working Hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website + "\n")

#else statement rewrites host file to original, meaning outside hours above you can access blocked sites

    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(5)

    #5 second delay when checking time