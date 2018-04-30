import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../../commentsData.db')

c = db.cursor()

c.execute("select section,ROUND(cast(count(c.assetURL) AS FLOAT) /count(distinct(webURL)),2) as Avrg from\
 (select section,webURL from articles group by section,webURL) as t1 LEFT OUTER JOIN\
 comments c ON c.assetURL=t1.webURL where section is not NULL and section <> 'false' and c.assetURL in (\
 select webURL from articles a,comments c\
 where a.webURL=c.assetURL group by webURL having count(*)>5 )\
 group by section order by Avrg")

print "queruy exec'ed"
sections = []
avgComments = []

for t in c.fetchall():
    sections.append(t[0])
    avgComments.append(t[1])

pos =  range(len(sections))

print max(avgComments)

rect1 = plt.bar(pos, avgComments, align= 'center')
plt.ylabel('Average Number of Comments')
plt.xlabel('Section Names')
plt.title('Average Number of Comments over Sections')
plt.xticks(pos, sections)
plt.xticks(rotation=90)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '{0:.1f}'.format(height),
                ha='center', va='bottom',fontsize= 8)

autolabel(rect1)

plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
