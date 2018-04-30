import sqlite3
import numpy as np
import os

#baseDIR = '/home/akshay/IIT KGP/SEM 2/Complex Network/Github/Complex-Term-Project/mappedLIWC_Male/'


db = sqlite3.connect('../commentsData.db')
c = db.cursor()

regions = ['South', 'MidWest', 'West','North East','U.S. territory','others']

sqlstat="select t.commentID,t.liwc  from commentsLIWC t, comments c, locationState ls where ls.city = c.userLocation and c.commentID = t.commentID  and t.gender = ? and ls.region = ?"

recp = 0

of = open('./regionWiseData.txt', 'w')

for gender in ['male', 'female']:
    for rg in regions:
        c.execute(sqlstat, (gender, rg))
        of.write(rg + ':\n\n')
        of.write(gender + '\n')
        sum =
        for res in c.fetchall():
            liwc = res[1]



            recp += 1
            if recp%100 == 0:
                print recp, "comments processed."

db.commit()
c.close()