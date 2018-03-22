import sqlite3
import sexmachine.detector as gender
import nltk
import string
from textblob import TextBlob

db = sqlite3.connect('../commentsData.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
#c.execute("create table if not exists maleComments(userID int,username text,comment text)")

#c.execute("insert into maleComments select A.userID, A.username, A.commentBody from comments A join commenterGender B where B.gender="male" and A.userID = B.userID and A.username = B.username")


c.execute("select userID, username, comment from femaleComments")

words_count = 0
comments_count = 0
file_count = 0
filename = "female_comments_"+str(file_count)+".txt"
file = open("./Female/" + filename, "wb")
# tags = []
# NN = 0
for result in c.fetchall():
    comment =result[2]
    tokens = nltk.word_tokenize(result[2].lower())
    token_count = 0
    for t in tokens:
        if t not in string.punctuation:
            token_count +=1 

    words_count += token_count
    
    
    # blob = TextBlob(comment)
    # #for sentence in blob.sentences:
    # for word,pos in blob.tags:
           
    #     if comments_count == 5:
    #         print word,pos
    #         if pos == NN:
    #             tags[pos] = 1

    # print tags[NN]
    comments_count += 1
    print comments_count
    if(comments_count%24000 == 0):
        file_count += 1
        filename = "female_comments_"+str(file_count)+".txt"
        file.close()
        file = open("./Female/" + filename, "wb")

    comment = comment.encode('ascii', 'ignore').decode('ascii')
    file.write(comment)
    file.write("\n\n\n")
    

    
    if(comments_count%100000==0):
        print comments_count," records processed"

print "Avg word_count per Female_Comment :"+str(words_count/comments_count)

db.commit()
c.close()