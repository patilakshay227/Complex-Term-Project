import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute("select section, count(*) as 'Count' from ArticleSection GROUP BY section ORDER BY Count")

sections = []
secCount = []

for t in c.fetchall():
    sections.append(t[0])
    secCount.append(t[1])



pos =  range(len(sections))
print max(secCount)

rect1 = plt.bar(pos, secCount, align= 'center')
plt.ylabel('No of Articles')
plt.xlabel('Section Names')
plt.title('Section Distribution over Articles')
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
#plt.savefig("SectionDistibution.png", bbox_inches='tight')
