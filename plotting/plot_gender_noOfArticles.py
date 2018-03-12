import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute("select C.userID, count(distinct C.assetURL) as artCount from comments C, commenterGender CG where C.userID = CG.userID and CG.gender =   'female' group by C.userID order by artCount desc;")

print "queruy exec'ed"
fuserids = []
farticlesCount = []

for t in c.fetchall():
    fuserids.append(t[0])
    farticlesCount.append(t[1])

pos =  range(len(fuserids))
print max(farticlesCount)

plt.plot(pos, farticlesCount, marker = '.', linewidth = 0, color = 'red', label = 'Female')


c.execute("select C.userID, count(distinct C.assetURL) as artCount from comments C, commenterGender CG where C.userID = CG.userID and CG.gender =   'male' group by C.userID order by artCount desc;")

muserids = []
marticlesCount = []

for t in c.fetchall():
    muserids.append(t[0])
    marticlesCount.append(t[1])

pos =  range(len(muserids))
print max(marticlesCount)

plt.plot(pos, marticlesCount, marker = '.', linewidth = 0, color = 'blue', label = 'Male')


#rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Articles')
plt.xlabel('Commenters')
plt.legend()
plt.title('Articles Distribution over Male and Female Commenters')
#plt.xticks(pos, userids)
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
