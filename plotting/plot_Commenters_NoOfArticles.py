import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

c.execute("SELECT A.webURL, COUNT(DISTINCT userID) as commCount from comments C,articles A where A.webURL = C.assetURL group by A.webURL order by commCount desc")

print "queruy exec'ed"
userids = []
articlesCount = []

for t in c.fetchall():
    articlesCount.append(t[1])

pos =  range(len(articlesCount))

print max(articlesCount)

plt.plot(pos, articlesCount, marker = '.', linewidth = 0)
#rect1 = plt.bar(pos, secCount, align= 'center')
plt.xlabel('Articles')
plt.ylabel('No of Commenters')
plt.title('Distribution of Commenters over Articles')

#plt.xticks(pos, userids)
plt.xticks(rotation=0)
#plt.yscale('log')
plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
