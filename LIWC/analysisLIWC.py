
import sqlite3
import os
import sys
from threading import Thread
import threading
reload(sys)
sys.setdefaultencoding('utf8')


baseDIR = '/home/akshay/IIT KGP/SEM 2/Complex Network/Github/Complex-Term-Project/Comments FOR LIWC/Male/'
liwcDIR = '/home/akshay/IIT KGP/SEM 2/Complex Network/Github/Complex-Term-Project/Results/male/'

count=0
tlock = threading.Lock()


def func1(f):
    global count
    db = sqlite3.connect('../../commentsData.db')

    c = db.cursor()

    fileName = baseDIR + f
    outFile = open("../mappedLIWC/id" + f, "w")
    liwcFile = open(liwcDIR + f.replace('.txt', '') + '_result.txt')
    liwcFile.readline()
    with open(fileName) as fo:
        for line in fo:
            line = line.strip()
            if len(line) == 0 or line == '':
                continue
            liwcLine = liwcFile.readline().split('\t', 1)[1]
            c.execute("select commentID from comments where commentBody like ?", ('%' + line + '%',))
            t = c.fetchone()
            if t is None:
                #print 'none', line
                continue
            #print t[0], liwcLine
            outFile.write(str(t[0]) + "\t\t" + liwcLine + '\n')
            with tlock as t:
                count+=1
                if count%100==0:
                    print "proccessed lines",count


    outFile.close()
    liwcFile.close()
    db.close()

#c.execute("select commentID from comments where commentBody = ?", (comment))
#files = sorted(os.listdir(baseDIR), key= lambda x: os.path.getctime(baseDIR+x))
threadslist=list()
print "DB connected"

for f in os.listdir(baseDIR):
    t = Thread(target=func1, args=(f,))
    threadslist.append(t)

for t in threadslist:
    t.start()
for t in threadslist:
    t.join()






