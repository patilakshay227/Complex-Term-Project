import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute("select s.section as 'SectionName',count(*) as 'CommentsCount' from comments c,articles a, ArticleSection s where c.assetURL=a.webURL and a.id=s.id group by s.section order by CommentsCount")

print "queruy exec'ed"
sections = []
secCount = []

for t in c.fetchall():
    sections.append(t[0])
    secCount.append(t[1])

pos =  range(len(sections))
print max(secCount)

rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Comments')
plt.xlabel('Section Names')
plt.title('Comments Distribution over Sections')
plt.xticks(pos, sections)
plt.xticks(rotation=90)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '%d'%int(height),
                ha='center', va='bottom', rotation = 90)

autolabel(rect1)


plt.show()
#plt.savefig('commentsDistribution.png', bbox_inches='tight')
