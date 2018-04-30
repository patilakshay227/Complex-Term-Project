import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3

db = sqlite3.connect('../../commentsData.db')
c = db.cursor()
db.text_factory = str


c.execute("create table if not exists locationState(city text,state text,region text,\
PRIMARY KEY(city,state))")

sqlstat="insert into locationState values(?,?,?)"
count=0;

with open("NonUs", "r") as r:
    for line in r:
        if len(line.strip()) == 0:
            continue
        try:

            c.execute(sqlstat, (line.split(";")[0], "others","others"))
            count+=1
        except sqlite3.IntegrityError as e:
            print  e, " execpt:", str(e)

db.commit()
db.close()
print (count)