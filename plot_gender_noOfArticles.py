import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute("select C.userID, count(distinct C.assetURL) as artCount from comments C, commenterGender CG where C.userID = CG.userID and CG.gender =   'female' group by C.userID order by artCount desc;")

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
plt.ylabel('No of Articles')
plt.xlabel('Female Commenters')
plt.title('Articles Distribution over Female Commenters')
#plt.xticks(pos, userids)
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
