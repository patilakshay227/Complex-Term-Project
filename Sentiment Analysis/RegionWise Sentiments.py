import json

import sqlite3
import sys
from textblob import TextBlob

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

locs = ['South', 'MidWest', 'West', 'North East', 'U.S. territory', 'others']

query = 'select c.commentBody,gender from locationState,comments c,posTags p,commenterGender t2 where city=userLocation and c.commentID=p.commentID \
and c.userID = t2.userID and c.username=t2.username and region=?'

result = open("SentResult.txt", "w")

dist = dict()
distm = dict()
distf = dict()


def getDist(gen,neu,pos,neg ):
    total = neu + pos + neg
    result.write("\n" + gen + "\t")
    result.write(str(float(neu)/total * 100) + '\t')
    result.write(str(float(pos)/total * 100)+'\t')
    result.write(str(float(neg)/total * 100))

count=0

for loc in locs:
    result.write("\n\n\n\n State : " + loc + "\n")
    print "query started for : ", loc
    qr = c.execute(query, (loc,))
    print "query finished"
    mtot=0
    ftot=0
    malePositive = 0
    maleNegative = 0
    maleNeutral = 0
    femalePositive = 0
    femaleNegative = 0
    femaleNeutral = 0

    for tr in qr.fetchall():
        comment=tr[0]
        gender=tr[1]

        com = TextBlob(comment)
        polar = com.sentiment.polarity

        if gender == 'male':
            mtot+=1
            if polar <= -0.2:
                maleNegative += 1
            elif polar >= 0.2:
                malePositive += 1
            else:
                maleNeutral += 1
        if gender == 'female':
            ftot+=1
            if polar <= -0.2:
                femaleNegative += 1
            elif polar >= 0.2:
                femalePositive += 1
            else:
                femaleNeutral += 1
        count+=1
        print "processed comments ",count

    getDist('Male',maleNeutral,malePositive,maleNegative)
    getDist('FeMale', femaleNeutral, femalePositive, femaleNegative)
result.close()