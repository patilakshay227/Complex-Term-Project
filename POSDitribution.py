#-------------------------------------------------------------------------------------
#Autor : Ami Ladani
#Functionalities : 1)Extracting genderwise comments
#                  2)POS tag distribution
#-------------------------------------------------------------------------------------
import sqlite3
import sexmachine.detector as gender
import nltk
import string
from textblob import TextBlob
GENDER = 'male'

db = sqlite3.connect('../commentsData.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
#c.execute("create table if not exists maleComments(userID int,username text,comment text)")

#c.execute("insert into maleComments select A.userID, A.username, A.commentBody from comments A join commenterGender B where B.gender="male" and A.userID = B.userID and A.username = B.username")


c.execute("select userID, username, comment from "+GENDER+"Comments")
tags = {'VERB':0,'NOUN':0,'PRON':0,'ADJ':0,'ADV':0, 'ADP':0,'CONJ':0,'DET':0,'NUM':0,'PRT':0,'X':0,'.':0}


words_count = 0
comments_count = 0
file_count = 0
filename = "./"+GENDER+"_comments/"+GENDER+"_comments_"+str(file_count)+".txt"
file = open(filename, "wb")
# tags = []
# NN = 0
for result in c.fetchall():
    comment =result[2]
    comment = comment.encode('ascii', 'ignore').decode('ascii')

    tokens = nltk.word_tokenize(result[2].lower())
    posTagged = nltk.pos_tag(tokens, tagset='universal')           

    for tag in posTagged:
        tags[tag[1]] += 1

    # token_count = 0
    # for t in tokens:
    #     if t not in string.punctuation:
    #         token_count +=1 
            
    # words_count += token_count
    # comments_count += 1
    # if(comments_count%24000 == 0):
    #     file_count += 1
    #     filename = "./"+GENDER+"_comments/"+GENDER+"_comments_"+str(file_count)+".txt"
    #     file.close()
    #     file = open(filename, "wb")
    
    # file.write(comment)
    # file.write("\n\n\n")
        
    print tags.items()

    if(comments_count%100000==0):
        print comments_count," records processed"

# print "Avg word_count per "+GENDER+"_Comment :"+str(words_count/comments_count)

del l['.']
count_tags = tags.items()

#count_tags = [('ADV', 738714), ('ADP', 1177188), ('DET', 1100886), ('VERB', 2161791), ('X', 15320), ('CONJ', 398224), ('ADJ', 1030634), ('NOUN', 2945142), ('PRT', 388112), ('PRON', 741393), ('NUM', 99730)]

total_tags = 0
for val in count_tags:
    total_tags += int(val[1])
print total_tags

percnt_tags = []

for val in count_tags:
    l = []
    l.append(val[0])
    temp = float(val[1])*100/total_tags
    l.append(temp)
    percnt_tags.append(l)

print percnt_tags
db.commit()
c.close()