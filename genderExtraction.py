import sqlite3
import sexmachine.detector as gender


db = sqlite3.connect('../commentdata.db')
d = gender.Detector(case_sensitive=False)
c = db.cursor()
c.execute("select userID,username from comments group by userID,username")

male=open("Male.txt","w")
female=open("Female.txt","w")
andy=open("Andy.txt","w")
mcount=0
fcount=0
acount=0
progress=0

for result in c.fetchall():
    id,name=str(result[0]),result[1]
    names=name.split()
    if len(names[0])==1 and len(names)>1:
        name=names[1]
    else:
        name=names[0]
    gen=d.get_gender(name)
    res=id+"\t"+result[1]+"\t"+gen+"\n"
    res=res.encode('utf-8')
    if gen=="male" or gen=="mostly_male" :
        male.write(res)
        mcount+=1
    elif gen=="female" or gen=="mostly_female":
        female.write(res)
        fcount+=1
    else:
        andy.write(res)
        acount+=1
    progress+=1
    if(progress%100000==0):
        print progress," records processed"

male.close()
female.close()
andy.close()
c.close()

with open("GenderCounts.txt","w") as g:
    g.write("Male count: "+str(mcount)+"\n")
    g.write("Female count: "+str(fcount) + "\n")
    g.write("Not Classified: "+str( acount )+ "\n")