import sqlite3
import sexmachine.detector as gender
import nltk
import string

db = sqlite3.connect('../../commentsData.db')
c = db.cursor()

c.execute("create table if not exists articleKeywords(webURL text,keyword text, PRIMARY KEY(webURL,keyword))")

sqlstat="insert into articleKeywords values(?,?)"

# c.execute("insert into maleComments select A.userID, A.username, A.commentBody from comments A join commenterGender B where B.gender="male" and A.userID = B.userID and A.username = B.username")


c.execute("select webURL, keywords from articles")

errCount = 0
proc = 0
for result in c.fetchall():
    url = result[0]
    keyword = result[1]
    if len(keyword.strip()) == 0:
        continue
    tokens = keyword.split(';')

    for kw in tokens:
        try:
            c.execute(sqlstat, (url, kw))
        except sqlite3.IntegrityError as e:
            errCount += 1

    proc += 1
    if proc % 1000 == 0:
        print "articles processed : ", proc

print errCount
db.commit()
c.close()