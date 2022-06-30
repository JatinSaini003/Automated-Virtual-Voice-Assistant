import time
import pandas as pd
from pandas.core.algorithms import mode
from pandas.io.parsers import read_csv

# REMINDER FUNCTION
def rem(text, query):
    a=0
    mint = 0
    sec = 0

    r = pd.read_csv('reminder.csv')
    hour = list(r['hour'])
    min = list(r['min'])

    #take time from query if he says 10 30
    for i in range(0,len(query)):
        if(query[i]==":"):
            a=i

    if("p.m." in query):
        query = query.replace("p.m.", "")
        hours =int(query[0:a])+12
        minutes=int(query[a+1:a+3])
        df = pd.DataFrame([[text, hours, minutes]])
        df.to_csv('reminder.csv', mode='a', index=False, header=False)
        return "done"

    elif("a.m." in query):
        query = query.replace("a.m.", "")
        hours =12-int(query[a-2:a])
        minutes=float(int(query[a+1:a+3]))
        df = pd.DataFrame([[text, hours, minutes]])
        df.to_csv('reminder.csv', mode='a', index=False, header=False)
        return "done"

    else:
        sp = "I didn't understand the time your are saying, please speak again"
        return sp


        

# TIMER FUNCTION
def timer(text, query):
    if("minutes" in query) or ("minute" in query):
        for i in range(0,len(query)):
            if(query[i]=="m" and query[i+1]=="i"):
                c=i
                print(c)
        minutes=int(query[c-2:c])
        time.sleep(minutes*60)
        return text
        #print(text)    