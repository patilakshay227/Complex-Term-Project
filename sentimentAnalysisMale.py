from textblob import TextBlob
import sqlite3

db = sqlite3.connect('../commentsData.db')
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS CommentSent (commentID int,sentiment int,gender text,PRIMARY KEY (commentID))")

c.execute("select commentBody,g.gender,commentID from comments c,commenterGender g where c.userID=g.userID and\
            c.username=g.username and gender='male' ")

sqlstat = "insert into CommentSent values(?,?,?)"

progress = 0

for t in c.fetchall():
    progress += 1
    comment = t[0]
    gen = t[1]
    comID = t[2]
    com = TextBlob(comment)

    polar = com.sentiment.polarity
    sent = 0
    if gen == 'male':
        if polar <= -0.2:
            sent = -1
        elif polar >= 0.2:
            sent = 1
        else:
            sent = 0

        c.execute(sqlstat, (comID, sent, 'male'))

    if progress % 10000 == 0:
        print progress, " Comments processed"

db.commit()
db.close()


