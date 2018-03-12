import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute("SELECT userID, COUNT(*) as CommentsCount from comments group by userID order by CommentsCount desc")

print "queruy exec'ed"
userids = []
commCount = []

for t in c.fetchall():
    userids.append(t[0])
    commCount.append(t[1])

pos =  range(len(userids))
print max(commCount)

plt.plot(pos, commCount, marker = '.', linewidth = 0)
#rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Comments')
plt.xlabel('Commenters')
plt.title('Comments Distribution over Commenters')
#plt.xticks(pos, userids)
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
