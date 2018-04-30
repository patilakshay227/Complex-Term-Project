import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

#c.execute("select C.userID, count(distinct A.section) as artCount from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and CG.gender = 'female' group by C.userID order by artCount desc;")
c.execute("select A.webURL, count(distinct C.userID) from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and C.username = CG.username and CG.gender = 'female'group by A.webURL order by count(distinct C.userID) desc")

print "queruy exec'ed"
fuserids = []
farticlesCount = []

for t in c.fetchall():
    fuserids.append(t[0])
    farticlesCount.append(t[1])

pos =  range(len(fuserids))
print max(farticlesCount)

plt.plot(pos, farticlesCount, marker = '.', linewidth = 0, color = 'red', label = 'Female')


#c.execute("select C.userID, count(distinct A.section) as artCount from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and CG.gender =   'male' group by C.userID order by artCount desc;")
c.execute("select A.webURL, count(distinct C.userID) from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and C.username = CG.username and CG.gender = 'male'group by A.webURL order by count(distinct C.userID) desc")


muserids = []
marticlesCount = []

for t in c.fetchall():
    muserids.append(t[0])
    marticlesCount.append(t[1])

pos =  range(len(muserids))
print max(marticlesCount)

plt.plot(pos, marticlesCount, marker = '.', linewidth = 0, color = 'blue', label = 'Male')


#rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No. of Commenters')
plt.xlabel('Articles')
plt.legend()
plt.title('Distribution of Male and Female Commenters over Articles')
#plt.xticks(pos, userids)
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
