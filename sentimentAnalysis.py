from textblob import TextBlob
import sqlite3

db = sqlite3.connect('./commentsData.db')
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


def updateCount(comment,gen):

    com=TextBlob(comment)

    polar=com.sentiment.polarity

    if gen == 'male':
        if polar <= -0.2:
            maleNegative+=1
        elif polar >= 0.2:
            malePositive+=1
        else:
            maleNeutral+=1
    if gen == 'female':
        if polar <= -0.2:
            femaleNegative += 1
        elif polar >= 0.2:
            femalePositive += 1
        else:
            femaleNeutral += 1


for t in c.fetchall():
    progress+=1
    updateCount(t[0],t[1])
    if progress%1000==0:
        print progress," Comments processed"

mmsg="male positive "+malePositive+" male negative "+maleNegative+" male neutral "+maleNeutral

fmsg="female positive "+femalPositive+" female negative "+femaleNegative+" female netural"+femaleNeutral

with open("male","w") as f:
	f.write(mmsg)

with open("female","w") as f:
	f.write(fmsg)

