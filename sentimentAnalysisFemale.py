from textblob import TextBlob
import sqlite3

db = sqlite3.connect('../commentsData.db')
c = db.cursor()

c.execute("select commentBody,g.gender from comments c,commenterGender g where c.userID=g.userID and\
            c.username=g.username and gender='female' ")

malePositive=0
maleNegative=0
maleNeutral=0
femalPositive=0
femaleNegative=0
femaleNeutral=0
progress=0

f=open("femaleSentiments","w")


for t in c.fetchall():
    progress+=1
    comment=t[0]
    gen=t[1]
    com=TextBlob(comment)

    polar=com.sentiment.polarity

    if gen == 'female':
        f.write(str(polar)+"\n")
          
    if progress%10000==0:
        print progress," Comments processed"
f.close()

