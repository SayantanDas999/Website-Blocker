# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:31:36 2019

@author: Sayantan
"""

""" Host file path Windows -> C:\Windows\System32\drivers\etc """
""" Host file path Mac/Linux -> /etc/hosts """

import time
from datetime import datetime as dt

hosts_temp = r"C:\Users\Sayantan\.spyder-py3\Projects\3-WebsiteBlocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","www.gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,1):
        print("Working Hours")
        with open(hosts_path,"r+") as myfile:
            content = myfile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    myfile.write("\n"+redirect+" "+website)
    else:
        print("Fun Hours")
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)

    