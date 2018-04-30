import nltk
import json
import sqlite3
import sys
import concurrent.futures
import threading
executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
futurelist=list()


db = sqlite3.connect('../../commentsData.db')
db.text_factory=str
c = db.cursor()

c.execute("create table if not exists posTags(commentID int,postTag text,PRIMARY KEY (commentID) ) ")

query="insert into posTags values (?,?) "

idFile=sys.argv[1]
commentFile=sys.argv[2]



def convertToDict(ltup):
    r=dict()
    for tup in ltup:
        key=tup[0]
        val=tup[1]
        if r.has_key(val):
            r[val].append(key)
        else:
            r[val]=list()
            r[val].append(key)

    s=json.dumps(r,ensure_ascii=False)

    return s


count=0
cfile=open(commentFile,"r")

def doWork(comment):
    global  count
    text = nltk.word_tokenize(comment)
    interm = nltk.pos_tag(text)
    res = convertToDict(interm)
    c.execute(query, (int(line), res))
    tlock = threading.Lock()
    with tlock as t:
        count += 1

        if count % 100 == 0:
            print "processed comments", count


with open(idFile) as ifile:
    for line in ifile:
        line=line.strip()

        comment=cfile.readline()
        comment=comment.decode('utf-8').strip()
        futurelist.append(executor.submit(doWork,(comment)))

for f in futurelist:
    f.done()

db.commit()
db.close()