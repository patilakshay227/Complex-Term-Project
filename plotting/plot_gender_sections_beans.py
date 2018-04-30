import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

c.execute("select C.userID, count(distinct A.section) as artCount from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and CG.gender =   'female' group by C.userID order by artCount desc;")

print "queruy exec'ed"

a=[]
freq=dict()
for i in range(0,11):
    a.append(i*2)


for t in c.fetchall():

    count  = t[1]
    for i in range(1, len(a)):
        if count > 20:
            if freq.has_key('>20'):
                freq['>20'] += 1
            else:
                freq['>20'] = 1
        if count > a[i - 1] and count <= a[i]:
            r = str(a[i - 1]) + '-' + str(a[i])
            if freq.has_key(r):
                freq[r] += 1
            else:
                freq[r] = 1

ind = range(len(freq))  # the x locations for the groups
width = 0.3       # the width of the bars


xvals = []
yvals = []
ftot = 0
for key in freq.keys():
    ftot+= freq[key]

skeys=[]
for key in freq.keys():
    if len(key.split("-")[0])==1 and key.split("-")[0]!='0':
        skeys.append('0'+key)
        freq['0' + key] = freq[key]
    else:
        skeys.append(key)



for e in sorted(skeys):
    xvals.append(e)
    yvals.append((freq[e]/float(ftot)) * 100)

print max(yvals)

rect1 = plt.bar(ind, yvals, width, align= 'center', color = 'red', label = 'Female')
plt.xticks(ind, xvals)
#plt.plot(pos, farticlesCount, marker = '.', linewidth = 0, color = 'red', label = 'Female')


c.execute("select C.userID, count(distinct A.section) as artCount from comments C, commenterGender CG, articles A where C.assetURL = A.webURL and C.userID = CG.userID and CG.gender =   'male' group by C.userID order by artCount desc;")

a=[]
freq=dict()
for i in range(0,11):
    a.append(i*2)
for t in c.fetchall():

    count  = t[1]
    for i in range(1, len(a)):
        if count > 100:
            if freq.has_key('>20'):
                freq['>20'] += 1
            else:
                freq['>20'] = 1
        if count > a[i - 1] and count <= a[i]:
            r = str(a[i - 1]) + '-' + str(a[i])
            if freq.has_key(r):
                freq[r] += 1
            else:
                freq[r] = 1

ind = range(len(freq))  # the x locations for the groups
width = 0.3       # the width of the bars

for i in ind:
    ind[i] += width

xvals = []
yvals = []

mtot = 0
for key in freq.keys():
    mtot+= freq[key]

skeys = []

for key in freq.keys():
    if len(key.split("-")[0])==1 and key.split("-")[0]!='0':
        skeys.append('0'+key)
        freq['0'+key] = freq[key]
    else:
        skeys.append(key)


for e in sorted(skeys):
    xvals.append(e)
    yvals.append((freq[e]/float(mtot)) * 100)

print max(yvals)

rect2 = plt.bar(ind, yvals, width, align= 'center', color = 'blue', label = 'Male')

# plt.plot(pos, marticlesCount, marker = '.', linewidth = 0, color = 'blue', label = 'Male')
#

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '{0:.1f}%'.format(height),
                ha='center', va='bottom',fontsize= 8, color = 'green')

autolabel(rect1)
autolabel(rect2)
# #rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Commenters')
plt.xlabel('No of Section Ranges')
plt.legend()
#plt.title('Frequecy of Articles Male Commenters')
plt.xticks(rotation=0)




plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
