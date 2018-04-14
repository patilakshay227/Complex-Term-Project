import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3

db = sqlite3.connect('../../commentsData.db')
c = db.cursor()
db.text_factory = str

c.execute("create table if not exists locationState(city text,state text,\
PRIMARY KEY(city,state))")
sqlstat="insert into locationState values(?,?)"

exclude = ['American Samoa', 'District of Columbia', 'Guam', 'Puerto Rico', 'United States Virgin Islands']

count = 0
s = list()
with open("Result", "r") as r:
    for line in r:
        state = line.split(";")[0]
        if state not in exclude:
            s.append(state)
            data = line.split(";")[1].split("\t")
            count += len(data)
            for d in data:
                try:

                    c.execute(sqlstat, (d,state))
                except sqlite3.IntegrityError as e:
                    print "key error on tuple ",state,e," execpt:",str(e)
db.commit()
db.close()

print count," records inserted"
print len(s)," states"
s = sorted(s)
for name in s:
    print name
