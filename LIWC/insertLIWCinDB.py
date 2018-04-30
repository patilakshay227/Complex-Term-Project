import sqlite3
import os

baseDIR = '/home/akshay/IIT KGP/SEM 2/Complex Network/Github/Complex-Term-Project/mappedLIWC_Male/'


db = sqlite3.connect('../commentsData.db')
c = db.cursor()
c.execute("create table if not exists commentsLIWC(commentID int,liwc text, gender text)")

sqlstat="insert into commentsLIWC values(?,?,?)"
recp = 0

for f in os.listdir(baseDIR):
    fileName = baseDIR + f
    with open(fileName) as fo:
        for line in fo:
            line = line.strip()
            if len(line) == 0:
                continue
            cid, liwc = line.split('\t\t')
            #print cid, liwc
            recp += 1
            c.execute(sqlstat, (cid, liwc, 'male'))


            if recp%100 == 0:
                print recp, "comments processed."

db.commit()
c.close()