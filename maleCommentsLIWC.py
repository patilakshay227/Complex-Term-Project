import sqlite3
import sexmachine.detector as gender
import nltk
import string

db = sqlite3.connect('../commentsData.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
#c.execute("create table if not exists maleComments(userID int,username text,comment text)")

#c.execute("insert into maleComments select A.userID, A.username, A.commentBody from comments A join commenterGender B where B.gender="male" and A.userID = B.userID and A.username = B.username")


c.execute("select userID, username, comment from maleComments")

words_count = 0
comments_count = 0
file_count = 0
filename = "male_comments_"+str(file_count)+".txt"
file = open(filename, "wb")

for result in c.fetchall():
    comment =result[2]
    tokens = nltk.word_tokenize(result[2].lower())
    token_count = 0
    for t in tokens:
        if t not in string.punctuation:
            token_count +=1 

    words_count += token_count

    comments_count += 1
    if(comments_count%24000 == 0):
        file_count += 1
        filename = "male_comments_"+str(file_count)+".txt"
        file.close()
        file = open(filename, "wb")

    comment = comment.encode('ascii', 'ignore').decode('ascii')
    file.write(comment)
    file.write("\n\n\n")
    

    if(comments_count%100000==0):
        print comments_count," records processed"
print "Avg word_count per Male_Comment :"+str(words_count/comments_count)

db.commit()
c.close()

# with open("GenderCounts.txt","w") as g:
#     g.write("Male count: "+str(mcount)+"\n")
#     g.write("Female count: "+str(fcount) + "\n")
#     g.write("Not Classified: "+str( acount )+ "\n")