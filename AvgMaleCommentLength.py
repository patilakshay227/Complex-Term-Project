import sqlite3
import nltk
import string

db = sqlite3.connect('../commentsData.db')
c = db.cursor()

c.execute("select commentBody,g.gender from comments c,commenterGender g where c.userID=g.userID and\
            c.username=g.username and gender='male' or gender='female' ")

totalWordsinMale=0
commentsByMale=0


totalWordsinFeMale=0
commentsByFeMale=0
progress=0

for t in c.fetchall():
    progress+=1
    rawtokens=nltk.word_tokenize(t[0])

    if t[1]=='male':
        commentsByMale+=1
    if t[1] == 'female':
        commentsByFeMale+= 1

    for w in rawtokens:
        if w not in string.punctuation:
            if t[1] == 'male':
                totalWordsinMale += 1
            if t[1] == 'female':
                totalWordsinFeMale += 1
    if progress%50000==0:
        print progress," Comments processed"

print "total words by male",totalWordsinMale," total comments by male",commentsByMale
print "total words by female",totalWordsinFeMale," total comments by male",commentsByFeMale

print "male avg words per comment",(totalWordsinMale/commentsByMale)
print "female avg words per comment",(totalWordsinFeMale/commentsByFeMale)