#!/usr/bin/env python
import pwd
import os
import sys
DIR =  sys.argv[1]
os.chdir(DIR)

def no_user():
    if folder == "nouser":
        pass
    else:
        os.system('mv %s %s' %(folder,"nouser"))


# find all folder in DIR
for folder in os.walk(DIR).next()[1]:
    stat_info = os.stat(folder)
    uid = stat_info.st_uid
    try:
        user = pwd.getpwuid(uid)[0]
    except:
        no_user()

    if user != folder:
        try:
            os.system('chown %s %s||echo 0'%s(folder,folder))
        except:
            no_user()

