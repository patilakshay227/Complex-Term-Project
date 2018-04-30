import json

import sqlite3
import sys

db = sqlite3.connect('../../commentsData.db')
db.text_factory=str
c = db.cursor()


locs=['South','MidWest','West','North East','U.S. territory','others']


query='select region,postTag,gender from locationState,comments c,posTags p,commenterGender t2 where city=userLocation and c.commentID=p.commentID \
and c.userID = t2.userID and c.username=t2.username and region=?'


result=open("postTagDis.txt","w")

dist=dict()
distm=dict()
distf=dict()

def getDist(region,dist,gen,ccount):
    r=list()
    total=0.0
    print ccount
    for k in dist.keys():
        r.append((k,dist[k]*1.0/ccount))
    r.sort(key=lambda x: x[0])
    result.write("\n"+gen+"\n")
    for t in r:
        result.write(t[0]+"\t")
    result.write("\n")
    for t in r:
        result.write(str(t[1])+"\t")


for loc in locs:
    result.write("\n\n\n\n State : "+loc+"\n")
    print "query started for : ",loc
    qr=c.execute(query,(loc,))
    print "query finished"
    tcount=0
    mcount=0
    fcount=0
    for tr in qr.fetchall():
        tags=json.loads(tr[1])
	tcount+=1
        #print tags
	if tr[2]=='male':
		mcount+=1
	if tr[2]=='female':
		fcount+=1
        for t in tags:

            if dist.has_key(t):
                dist[t]+=1
            else:
                dist[t]=1
            if tr[2]=='male':
                if distm.has_key(t):
                    distm[t] += 1
                else:
                    distm[t] = 1
		
            if tr[2]=='female':
                if distf.has_key(t):
                    distf[t] += 1
                else:
                    distf[t] = 1
		

    getDist(loc,dist,'All',tcount)
    getDist(loc, distm,'Male',mcount)
    getDist(loc, distf,'Female',fcount)
    print loc, "done"

    dist=dict()
    distm=dict()
    distf=dict()
    r = list()
result.close()
