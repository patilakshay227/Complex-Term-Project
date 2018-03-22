import sqlite3
import sexmachine.detector as gender
import nltk
import string

db = sqlite3.connect('../commentsData.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
#c.execute("create table if not exists maleComments(userID int,username text,comment text)")

#c.execute("insert into maleComments select A.userID, A.username, A.commentBody from comments A join commenterGender B where B.gender="male" and A.userID = B.userID and A.username = B.username")


c.execute("select userID, username, comment from femaleComments")

words_count = 0
comments_count = 0

for result in c.fetchall():
    comment =result[2]
    tokens = nltk.word_tokenize(result[2].lower())
    token_count = 0
    for t in tokens:
        if t not in string.punctuation:
            token_count +=1 

    words_count += token_count
    comments_count += 1
    if(comments_count%100000==0):
        print comments_count," records processed"
        
print "Avg word_count per Female_Comment :"+str(words_count/comments_count)

db.commit()
c.close()