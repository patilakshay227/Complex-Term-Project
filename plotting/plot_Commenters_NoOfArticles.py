import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

c.execute("SELECT C.userID, COUNT(DISTINCT assetURL) as ArticlesCount from comments C,articles A where A.webURL = C.assetURL group by userID order by ArticlesCount desc")

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
plt.xlabel('Commenters')
plt.title('Frequency of Articles over Commenters')

#plt.xticks(pos, userids)
plt.xticks(rotation=0)
plt.yscale('log')
plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
