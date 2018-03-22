import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

c.execute("SELECT C.userID, count(distinct section) as secCount from comments C, articles A where C.assetURL = A.webURL and section is not null group by C.userID  having secCount >= 5 order by secCount desc")

print "queruy exec'ed"
userids = []
articlesCount = []

for t in c.fetchall():
    userids.append(t[0])
    articlesCount.append(t[1])

pos =  range(len(userids))
print max(articlesCount)

plt.plot(pos, articlesCount, marker = '.', linewidth = 0)
#rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Sections')
plt.xlabel('Commenters')
plt.title('Frequency of Sections over Commenters')
#plt.xticks(pos, userids)
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
