import sqlite3
import sexmachine.detector as gender


db = sqlite3.connect('../commentsData.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
c.execute("create table if not exists commenterGender(userID int,username text,gender text,\
PRIMARY KEY(userID,username))")
c.execute("select userID,username from comments group by userID,username")

sqlstat="insert into commenterGender values(?,?,?)"

mcount=0
fcount=0
acount=0
progress=0

for result in c.fetchall():
    id,name=result[0],result[1]
    names=name.split()
    if len(names[0])==1 and len(names)>1:
        name=names[1]
    else:
        name=names[0]
    gen=d.get_gender(name)
    if gen=="male" or gen=="mostly_male" :
        c.execute(sqlstat,(id,result[1],"male"))
        mcount+=1
    elif gen=="female" or gen=="mostly_female":
        c.execute(sqlstat,( id, result[1], "female"))
        fcount+=1
    else:
        c.execute(sqlstat, (id, result[1], "andy"))
        acount+=1
    progress+=1
    if(progress%100000==0):
        print progress," records processed"

db.commit()
c.close()

with open("GenderCounts.txt","w") as g:
    g.write("Male count: "+str(mcount)+"\n")
    g.write("Female count: "+str(fcount) + "\n")
    g.write("Not Classified: "+str( acount )+ "\n")