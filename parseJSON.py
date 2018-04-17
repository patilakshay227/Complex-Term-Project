import tarfile
import sys
import io
import os
import gzip
import json
import re
import pickle as pk
import time
import ast
import HTMLParser

start = time.time()

fileName = './dailyArticles.txt'

f = open(fileName)
of = open('dailyCommentJSON.txt', 'w')

# for line in f:
#     dic = json.loads(line)
#     #print len(dic['results']['comments'])
#     print dic.keys()
#     break

fs = 0
for lines in f:
    line = lines.rsplit('\t',2)[2]
    try:
        obj = json.loads(line)
        json.dump(obj, fp=of)
        of.write('\n')
    except:
        obj = json.loads(json.dumps(ast.literal_eval(line)))
        json.dump(obj, fp=of)
        of.write('\n')
        # fs+=1
        # print "{} files skipped".format(fs)
        # continue





totalTime = time.time() - start
m, s = divmod(totalTime, 60)
print "Total Time Taken %d Min %d Seconds" % (m, s)
